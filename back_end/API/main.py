import uvicorn
from fastapi import FastAPI
from .routers.tasks import get_tasks, create_task
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

def main():
    app = FastAPI()
    # Especificando as origens permitidas
    app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
            )
    # Pegar a lista de tarefas do usuario
    @app.get('/tasks/')
    async def list_tasks():
        return await get_tasks()

    @app.get('/tasks/new_task/')
    async def add_task(descr: str, date_time: str):
        return await create_task(descr_task=descr, datetime_task=date_time)
    
    return app
if __name__ == '__main__':
    uvicorn.run(
            "back_end.API.main:main",
            port=8080
            )
