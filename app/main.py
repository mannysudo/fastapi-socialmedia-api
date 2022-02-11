#Virtual Environment Set Up 
#Use VENV to containarize resources and utilize them uniquely to each project

#import dependecies
from typing import Optional, List
from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from . import models, schemas, utils
from .database import *
from starlette.responses import Response
from sqlalchemy.orm import Session
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI() #create instance to use FastAPI

#dummy data
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

##################################

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")       #function decorator - standardized notation
def root():   #functino name - customized notation
    return {"message": "Hello World"}

