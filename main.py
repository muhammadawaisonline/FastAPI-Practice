from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()
@app.get("/")
def index():
    return {"message":"Hello world"}

@app.get("/blog/all")
def get_blog2(page=1, page_size: Optional[int] = None):
    return {"message": f" all {page_size} blogs on {page} page"}

@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": f"blog with id {id}"}
class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def blog_type(type: BlogType):
    return {"message": f"blog type {type}"}



