import { get_tasks, add_task, mark_task } from "./request_manager.js";

async function addTask(){
        const descr_task = document.getElementById('descr').value;
        const date_task = document.getElementById('date').value;
        const time_task = document.getElementById('time').value;

        const datetime_task = date_task + ' ' + time_task;
        await add_task(descr_task, datetime_task);
}

async function markTask(event){
    const taskId = event.currentTarget.dataset.taskId;
    const btn = event.target;
    var task_is_done = 'O';

    if (btn.innerHTML == 'X'){
        btn.innerHTML = 'O';
        task_is_done = false;
    }else{
        btn.innerHTML = 'X';
        task_is_done = true
    }

    await mark_task(taskId, task_is_done);
}

const task_table = document.getElementById('task_table');
const btn_addTask = document.getElementById('btn_addTask');
const list_tasks = await get_tasks();

btn_addTask.addEventListener('click', addTask);

for (const task of list_tasks){
    const new_line = document.createElement('tr');

    var task_is_done = 'O';

    if(task.done){
        task_is_done = 'X';
    }

    new_line.innerHTML = ` 
    <td>${task.description}</td>
    <td>${task.date}</td>
    <td><button class='btn_markTask' data-task-id="${task.id}">${task_is_done}</button></td>
    `;

    task_table.appendChild(new_line);
}

const btn_markTask = document.querySelectorAll('.btn_markTask');

btn_markTask.forEach(btn => {btn.addEventListener('click', markTask)});
