from fastapi import FastAPI
from db import models
from db.database import engine
from routers import posts

app = FastAPI()

app.include_router(posts.router)

models.Base.metadata.create_all(engine)