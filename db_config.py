from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

database_user = os.getenv('DATABASE_USER','')
database_pwd = os.getenv('DATABASE_PASSWORD','')
database_name = os.getenv('DATABASE_NAME','')

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@localhost:3306/{}".format(
    database_user,
    database_pwd,
    database_name
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()