import time

from r_openai import util
from r_openai.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from r_openai.error import TryAgain


class Engine(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "engine"

    def generate(self, timeout=None, **params):
        start = time.time()
        while True:
            try:
                return self.request(
                    "post",
                    self.instance_url() + "/generate",
                    params,
                    stream=params.get("stream"),
                    plain_old_data=True,
                )
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for snapshot to warm up", error=e)

    def search(self, **params):
        return self.request("post", self.instance_url() + "/search", params)
