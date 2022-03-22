#Virtual Environment Set Up 
#Use VENV to containarize resources and utilize them uniquely to each project

#import dependecies
from fastapi import FastAPI
from . import models
from .database import *
from .routers import post, user, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI() #create instance to use FastAPI

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")       #function decorator - standardized notation
def root():         #functino name - customized notation
    return {"message": "Hello World"}

