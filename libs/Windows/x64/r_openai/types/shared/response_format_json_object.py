# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from r_typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResponseFormatJSONObject"]


class ResponseFormatJSONObject(BaseModel):
    type: Literal["json_object"]
    """The type of response format being defined: `json_object`"""
