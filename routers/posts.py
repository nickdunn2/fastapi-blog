from typing import List
from fastapi import APIRouter, Depends
from routers.schemas import PostBase, PostDisplay 
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_post

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/", response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


@router.post("/", response_model=PostDisplay)
def create_post(post: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(post, db)
