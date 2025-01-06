from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)
class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title:str
    content:str
    nb_comments:int
    published:Optional[bool]
    tags:List[str] = []
    metadata:Dict[str, str] = {"key1":"val1"}
    image:Optional[Image] = None

@router.post("/new/{id}")
def create_blog(blog: BlogModel, id:int, version:int = 1):
    blog.title
    return {
        "id":id,
        "version":version,
        "data":blog}

@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id:int, comment_title: int =Query(

    title = "Id of the comment",
    description= "Some description of the comment_id",
    alias= "commentId"
), 
    content:str = Body(...,
                       regex= "^[a-z\s]*$") ,
                       v: Optional[List[str]] = Query(["1.0", "1.1", "1.2 "]),
                       comment_id: int = Path( gt=5, le=10)):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id
    }

def required_functionality():
    return {"message": "learn FASTAPI is important"}



