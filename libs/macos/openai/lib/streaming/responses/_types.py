from __future__ import annotations

from r_typing_extensions import TypeAlias

from ....types.responses import ParsedResponse

ParsedResponseSnapshot: TypeAlias = ParsedResponse[object]
"""Snapshot type representing an in-progress accumulation of
a `ParsedResponse` object.
"""
