import time

from r_openai import util
from r_openai.api_resources.abstract import DeletableAPIResource, ListableAPIResource
from r_openai.api_resources.abstract.engine_api_resource import EngineAPIResource
from r_openai.error import TryAgain


class Completion(EngineAPIResource):
    OBJECT_NAME = "completions"

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new completion for the provided prompt and parameters.

        See https://beta.openai.com/docs/api-reference/completions/create for a list
        of valid parameters.
        """
        start = time.time()
        timeout = kwargs.pop("timeout", None)

        while True:
            try:
                return super().create(*args, **kwargs)
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)
