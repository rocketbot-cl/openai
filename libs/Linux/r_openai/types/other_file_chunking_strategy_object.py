# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from r_typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OtherFileChunkingStrategyObject"]


class OtherFileChunkingStrategyObject(BaseModel):
    type: Literal["other"]
    """Always `other`."""
