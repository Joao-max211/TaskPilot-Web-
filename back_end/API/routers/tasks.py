from ...database.commandsDB import query_tasks 

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
   

