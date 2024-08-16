# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from r_typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VectorStoreDeleted"]


class VectorStoreDeleted(BaseModel):
    id: str

    deleted: bool

    object: Literal["vector_store.deleted"]