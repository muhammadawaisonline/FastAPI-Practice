from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
from db import models
from db.database import engine
from routers import user



app = FastAPI()
@app.get("/hello")
def index():
    return {"message":"Hello world"}
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


models.Base.metadata.create_all(engine)







