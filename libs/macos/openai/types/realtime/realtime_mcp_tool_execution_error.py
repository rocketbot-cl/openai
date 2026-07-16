# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from r_typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RealtimeMcpToolExecutionError"]


class RealtimeMcpToolExecutionError(BaseModel):
    message: str

    type: Literal["tool_execution_error"]
