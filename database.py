from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = 'postgresql://postgres:postgres1234@localhost:5432/QuizApp'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
