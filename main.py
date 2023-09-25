

from typing import Optional
from fastapi import FastAPI  , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] =None
   

my_posts = [{"title" : "title of post 1 " , "content" : "content of post 1" , "id" : 1}  , {"title" : "favorite food" , "content" : "I like pizza" , "id" :2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
@app.get("/")
def root():
    return {"message": "welcome to my api !!!"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(Post: post):

    post_dict = Post.dict()
    post_dict['id'] = randrange(0,1000000)

    my_posts.append(post_dict)

    return {"data" : post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post =my_posts[len(my_posts)-1]
    return {"detail" : post}


@app.get("/posts/{id}")
def get_post(id : int):

    
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=  f"post with id: {id} was not found ")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message' : f"post with id: {id} was not found "}
    return{"post_detail" : post}
    
# title str , content str , category , Bool

