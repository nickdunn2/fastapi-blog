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


