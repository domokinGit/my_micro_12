import uuid

from pydantic import BaseModel


class PostUser(BaseModel):
    name: str
    email: str
    password: str


class User(PostUser):
    user_id: uuid.UUID
