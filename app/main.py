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
from . import models, schemas
from .database import *
from starlette.responses import Response
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI() #create instance to use FastAPI

### DATABASE CONNECTION ###
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='MMartx$5pst', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successful')
        break

    except Exception as error:
        print('Connection to database failed')
        print('Error: ', error)
        time.sleep(2)
        

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
def root():   #functino name - customized notation
    return {"message": "Hello World"}

@app.get('/posts', response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post).all()
    return posts

@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    # new_post = models.Post(**post.dict())
    # db.add(new_post)
    # db.commit()
    # db.refresh(new_post)

    return new_post

@app.get('/posts/{id}', response_model=schemas.Post)     #id field is called a path parameter
def get_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found') 
    return post

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    #edge case if post DNE
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')

    post.delete(synchronize_session=False)  
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}', response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    #edge case if post DNE
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()