# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from r_typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TextContent"]


class TextContent(BaseModel):
    """A text content."""

    text: str

    type: Literal["text"]
