# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from r_typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionMessageToolCallParam", "Function"]


class Function(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class ChatCompletionMessageToolCallParam(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    function: Required[Function]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""
