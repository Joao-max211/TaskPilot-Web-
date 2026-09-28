from datetime import datetime

from ...database.commandsDB import query_tasks, insert_newTask

async def get_tasks() -> list:
    tasks = await query_tasks()
    task_list = []
    for task in tasks:
        task_info = {
                'id': task.id,
                'description': task.task_descrition,
                'done': task.done,
                'date': str(task.date)
                }
        task_list.append(task_info)
    return task_list
   

async def create_task(descr_task: str, datetime_task: str):
    date_time = datetime.strptime(datetime_task, '%Y-%m-%d %H:%M')
    await insert_newTask(new_taskDescr=descr_task, new_taskDatetime=date_time)
