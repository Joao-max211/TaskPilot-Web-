from sqlalchemy.orm import sessionmaker
from .conectionDB import engine
from .models import Task

Session = sessionmaker(engine)

async def query_tasks():
    with Session() as session:
        return session.query(Task).all()
        
