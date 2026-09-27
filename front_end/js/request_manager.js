export async function get_tasks(){
    const request_task_list = await fetch('http://localhost:8080/tasks');

    if (request_task_list.ok) {
        return await request_task_list.json();
    }
    
    console.log('status: ', request_task_list.status);
}

get_tasks()
