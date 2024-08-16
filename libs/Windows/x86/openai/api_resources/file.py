from __future__ import absolute_import, division, print_function

import r_openai as openai
from r_openai import api_requestor, util
from r_openai.api_resources.abstract import (
    DeletableAPIResource,
    ListableAPIResource,
)


class File(ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "file"

    @classmethod
    def create(
        cls, api_key=None, api_base=None, api_version=None, organization=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=api_base or openai.file_api_base or openai.api_base,
            api_version=api_version,
            organization=organization,
        )
        url = cls.class_url()
        supplied_headers = {"Content-Type": "multipart/form-data"}
        response, _, api_key = requestor.request(
            "post", url, params=params, headers=supplied_headers
        )
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )
