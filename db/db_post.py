from fastapi import HTTPException, status
from routers.schemas import PostBase
from db.models import DbPost
from sqlalchemy.orm.session import Session
import datetime


def get_all_posts(db: Session):
  return db.query(DbPost).all()


def create_post(request: PostBase, db: Session):
  new_post = DbPost(
      title=request.title,
      content=request.content,
      image_url=request.image_url,
      creator=request.creator,
      created_at=datetime.datetime.now()
  )

  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  
  return new_post


def delete_post(id: int, db: Session):
  post = db.query(DbPost).filter(DbPost.id == id).first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
  
  db.delete(post)
  db.commit()

  return "successfully deleted"
