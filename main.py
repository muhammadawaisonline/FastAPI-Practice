from fastapi import FastAPI, Request
from routers import blog_get
from routers import blog_post
from db import models
from routers import article
from db.database import engine
from routers import user
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from routers import product


app = FastAPI()
@app.get("/hello")
def index():
    return {"message":"Hello world"}
app.include_router(user.router)
app.include_router(product.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request,  exc: StoryException):
    return JSONResponse(
        status_code=418,
        content= { "detail": exc.name}
    )
@app.exception_handler(StoryException)
def custom_handler(request: Request, exc:StoryException):
    return PlainTextResponse(str(exc), status_code= 400)


models.Base.metadata.create_all(engine)







