from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URI = "mysql+pymysql://root:Side1912*@localhost:3306/dados_projeto"

engine = create_engine(DATABASE_URI, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    return SessionLocal()
