#Virtual Environment Set Up 
#Use VENV to containarize resources and utilize them uniquely to each project

#import dependecies
from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange

from starlette.responses import Response

app = FastAPI() #create instance to use FastAPI

#POST class will extend BaseModel
#FastAPI will validate data passed to it based on this schema
class Post(BaseModel): 
    title: str      #set default data type for property
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

#Overview of HTTP requests types 
#GET - retrieve data from server
#POST - Establishes new information on the server to store/manipulate

# --- auxilary functions ---- #
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")       #function decorator - standardized notation
async def root():   #functino name - customized notation
    return {"message": "Hello World"}

@app.get('/posts')
def get_posts():
    return {'data': my_posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {'data': my_posts}

#contents for POST request to standardize front/back end formats
#title str, content str

@app.get('/posts/{id}')     #id field is called a path parameter
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND 
        return {'message': f'post with id: {id} was not found'}
    return {"post_detail": post}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    #edge case if post DNE
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)

    #edge case if post DNE
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}