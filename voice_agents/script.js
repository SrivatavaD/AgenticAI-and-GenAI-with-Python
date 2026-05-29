function addTask() {
    const input = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');
    const value = input.value.trim();

    if (!value) return;

    const li = document.createElement('li');
    const taskText = document.createElement('span');
    taskText.textContent = value;
    li.appendChild(taskText);

    li.onclick = function() { this.classList.toggle('completed'); };

    const del = document.createElement('button');
    del.textContent = 'Delete';
    del.className = 'delete-btn';
    del.type = 'button';
    del.onclick = function(e) {
        e.stopPropagation();
        li.remove();
    };

    li.appendChild(del);
    taskList.appendChild(li);
    input.value = '';
    input.focus();
}

document.getElementById('todoForm').addEventListener('submit', function(e) {
    e.preventDefault();
    addTask();
});
