from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from .conectionDB import engine

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task_descrition = Column(String(50), nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    date = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)

