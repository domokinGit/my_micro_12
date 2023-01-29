import uuid

from pydantic import BaseModel


class PostProduct(BaseModel):
    product: str
    price: int


class Product(PostProduct):
    product_id: uuid.UUID

