import uvicorn
from fastapi import FastAPI
from .routers.tasks import get_tasks
from fastapi.middleware.cors import CORSMiddleware

def main():
    app = FastAPI()
    # Especificando as origens permitidas
    app.add_middleware(
            CORSMiddleware,
            allow_origins=['http://localhost:8000'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
            )
    # Pegar a lista de tarefas do usuario
    @app.get('/tasks')
    async def list_tasks():
        return await get_tasks()
    
    return app
if __name__ == '__main__':
    uvicorn.run(
            "back_end.API.main:main",
            port=8080
            )
