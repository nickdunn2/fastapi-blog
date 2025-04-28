from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    image_url: str
    creator: str

class PostDisplay(BaseModel):
    id: int
    title: str
    content: str
    image_url: str
    creator: str
    created_at: datetime

    class Config:
        orm_mode = True