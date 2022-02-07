#Script will hande database connectivity
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false, true

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:MMartx$5pst@localhost/fastapi'

#instance of sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=false, autoflush=false, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()