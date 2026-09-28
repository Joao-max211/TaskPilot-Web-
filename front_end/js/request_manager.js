export async function get_tasks(){
    const request_task_list = await fetch('http://localhost:8080/tasks/');

    if (request_task_list.ok) {
        return await request_task_list.json();
    }    
}

export async function add_task(task_descr, task_datetime){
    const params = new URLSearchParams({
        descr: task_descr,
        date_time: task_datetime
    });

    await fetch(`http://localhost:8080/tasks/new_task/?${params}`);
}

