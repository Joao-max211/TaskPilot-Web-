from datetime import datetime

from sqlalchemy.orm import sessionmaker
from .conectionDB import engine
from .models import Task

Session = sessionmaker(engine)

async def query_tasks():
    with Session() as session:
        return session.query(Task).all()

async def insert_newTask(new_taskDescr:str, new_taskDatetime:datetime):
    with Session() as session:
        new_task = Task(
                task_descrition=new_taskDescr,
                date = new_taskDatetime
                )
        session.add(new_task)
        session.commit()
        
