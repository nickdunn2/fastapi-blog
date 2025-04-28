from .database import Base
from sqlalchemy import Column, DateTime, Integer, String

class DbPost(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    content = Column(String)
    image_url = Column(String)
    creator = Column(String)
    created_at = Column(DateTime)