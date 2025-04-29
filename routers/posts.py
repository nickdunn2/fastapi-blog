import string
import random
import shutil
from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
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


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    return db_post.delete_post(id, db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit('.', 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "filename": path
    }