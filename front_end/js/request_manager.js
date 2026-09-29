const url = 'http://localhost:8080'

export async function get_tasks(){
    const request_task_list = await fetch(url+'/tasks/');

    if (request_task_list.ok) {
        return await request_task_list.json();
    }    
}

export async function add_task(task_descr, task_datetime){

    const params = new URLSearchParams({
        descr: task_descr,
        date_time: task_datetime
    });

    await fetch(url+`/tasks/new_task/?${params}`, {
        method: 'POST'
    });
}

export async function mark_task(task_id, done){
    await fetch(url+`/tasks/${task_id}/?done=${done}`, {
        method: 'PUT'
    })
}

