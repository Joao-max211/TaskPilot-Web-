import { get_tasks } from "./request_manager.js";

const table = document.getElementById('table');
const list_tasks = await get_tasks();

for (const task of list_tasks){
    const new_line = document.createElement('tr');

    new_line.innerHTML = ` 
    <td>${task.description}</td>
    <td>${task.done}</td>
    <td>${task.date}</td>
    `;

    table.appendChild(new_line);
}
