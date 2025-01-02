from enum import Enum
from typing import Optional
from fastapi import Response, status, APIRouter
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

# @router.get("/blog/all")
# def get_blog2(page=1, page_size: Optional[int] = None):
#     return {"message": f" all {page_size} blogs on {page} page"}

@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog id {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog with id {id}"}

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}",
            summary= "Retrieve all blogs",
            description="Retrieve all Blogs based on Type"

            )
def blog_type(type: BlogType):
    return {"message": f"blog type {type}"}

@router.get("/{id}/comment/{comment_id}", tags=["comment"])
def get_comment(id:int, comment_id:int, valid:bool=True, username: Optional[str]= None ):
    """
    Stimuste retrieving content from Blog

    - **id** manadatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** Optional query parameter
    - **username** Optional query parameter
    """

    return {"message": f"In blog No.{id} comment {comment_id} is {valid} provided by user {username}"}