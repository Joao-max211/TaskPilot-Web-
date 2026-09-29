from datetime import datetime

from sqlalchemy import select
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


async def update_task_value(task_id:int, **values):
    with Session() as session:
        query = select(Task).where(Task.id == task_id)
        result = session.execute(query)
        task = result.scalar_one_or_none()

        for attribute, value in values.items():
            setattr(task, attribute, value)

        session.commit()

        
