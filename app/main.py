#Virtual Environment Set Up 
#Use VENV to containarize resources and utilize them uniquely to each project

#import dependecies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import *
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine) // creates tables in the traditional way, use Alembic instead

app = FastAPI() #create instance to use FastAPI

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],        #type of requests allowable
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")       #function decorator - standardized notation
def root():         #functino name - customized notation
    return {"message": "Hello World"}

