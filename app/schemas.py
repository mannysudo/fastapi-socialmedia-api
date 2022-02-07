#File will contain project schemas
from datetime import datetime
from pydantic import BaseModel

#FastAPI will validate data passed to it based on this schema
#sets default data type for property
class PostBase(BaseModel): 
    title: str              
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True