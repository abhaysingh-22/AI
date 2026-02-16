from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

# note that fast api execute line by line hence to pass these paths we need to be careful with the order specially with dynamic routing

@app.get("/")
def index():
    # return "hello world"
    return {"message": "hello world"}

@app.get("/about")
def info():
    return {"message": "Hey welcome to my about page"}

@app.get("/blog/{id}")   # this is known as dynamic routing
def blog_post(id: int):    # not necessary to specify the type here
    return {"message": f"Welcome to the blog post {id}"}  # this way we can set a variable to a url or path

@app.get("/blog/{id}/comments/{comment_id}")
def blog_comments(id: int, comment_id: int):
    return {"message": f"Welcome to the comments section of blog post {id}, comment {comment_id}"}


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@app.post("/blog")
def create_blog_post(post: Blog):
    return {"message": "Blog post created", "post": post}


# this is the basics of fastapi, that how to write a simple api with get and post request!!
