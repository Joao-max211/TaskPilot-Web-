import { get_tasks, add_task } from "./request_manager.js";

async function addTask(){
        const descr_task = document.getElementById('descr').value;
        const date_task = document.getElementById('date').value;
        const time_task = document.getElementById('time').value;

        const datetime_task = date_task + ' ' + time_task;
        await add_task(descr_task, datetime_task);
}

const task_table = document.getElementById('task_table');
const btn_addTask = document.getElementById('btn_addTask');
const list_tasks = await get_tasks();

btn_addTask.addEventListener('click', addTask);

for (const task of list_tasks){
    const new_line = document.createElement('tr');

    var task_is_done = '[ ]';
    if(task.done){
        task_is_done = '[X]';
    }

    new_line.innerHTML = ` 
    <td>${task.description}</td>
    <td>${task.date}</td>

    <td>${task_is_done}</td>
    `;

    task_table.appendChild(new_line);
}

