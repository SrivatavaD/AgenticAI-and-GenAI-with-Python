document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    let todos = JSON.parse(localStorage.getItem('todos')) || [];

    function saveTodos() {
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function renderTodos() {
        todoList.innerHTML = '';
        todos.forEach((todo, index) => {
            const li = document.createElement('li');
            if (todo.completed) li.classList.add('completed');

            const span = document.createElement('span');
            span.textContent = todo.text;
            span.style.cursor = 'pointer';
            span.addEventListener('click', () => toggleTodo(index));

            const btnGroup = document.createElement('div');
            btnGroup.className = 'btn-group';

            const editBtn = document.createElement('button');
            editBtn.textContent = 'Edit';
            editBtn.className = 'edit-btn';
            editBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                editTodo(index);
            });

            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.className = 'delete-btn';
            deleteBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                deleteTodo(index);
            });

            btnGroup.appendChild(editBtn);
            btnGroup.appendChild(deleteBtn);
            li.appendChild(span);
            li.appendChild(btnGroup);
            todoList.appendChild(li);
        });
    }

    function addTodo(e) {
        e.preventDefault();
        const text = todoInput.value.trim();
        if (text) {
            todos.push({ text, completed: false });
            saveTodos();
            renderTodos();
            todoInput.value = '';
        }
    }

    function toggleTodo(index) {
        todos[index].completed = !todos[index].completed;
        saveTodos();
        renderTodos();
    }

    function editTodo(index) {
        const newText = prompt('Edit your task:', todos[index].text);
        if (newText !== null) {
            const trimmed = newText.trim();
            if (trimmed) {
                todos[index].text = trimmed;
                saveTodos();
                renderTodos();
            }
        }
    }

    function deleteTodo(index) {
        todos.splice(index, 1);
        saveTodos();
        renderTodos();
    }

    todoForm.addEventListener('submit', addTodo);
    renderTodos();
});