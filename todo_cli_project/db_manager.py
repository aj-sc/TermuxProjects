import json
from datetime import datetime

FILE_PATH = 'database.json'

def write_data(data : list, path : str = FILE_PATH) -> None:
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def get_data(path : str = FILE_PATH) -> list:
    try:
        with open(path, 'r') as file:
            file_content = json.load(file)

        return file_content
    except FileNotFoundError:
        write_data([])

        return []

def add_todo(task : str) -> None:
    try:
        todos = get_data()

        todo_id = todos[-1].get('todo_id', 0) + 1 if todos else 1

        new_todo = {
                'todo_id' : todo_id,
                'task' : task,
                'status' : 'active',
                'is_done' : False,
                'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'completed_at' : None
                }

        todos.append(new_todo)
        write_data(todos)

        return True
    except Exception as err:
        print('Error: ', err)
        return False

def complete_todo(todo_index : int) -> None:
    try:
        todos = get_data()
        active_todos = get_active_todos(todos)

        active_todos[todo_index - 1]['is_done'] = True
        active_todos[todo_index - 1]['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        write_data(todos)

        return True
    except Exception as err:
        print('Error: ', err)
        return False

def delete_todo(todo_index : int) -> None:
    try:
        todos = get_data()
        active_todos = get_active_todos(todos)

        active_todos[todo_index - 1]['status'] = 'inactive'

        write_data(todos)

        return True
    except Exception as err:
        print('Error: ', err)
        return False

def get_completed_todos(todos : list = None) -> list:
    if todos is None:
        todos = get_data()

    return [todo for todo in todos if todo['is_done'] == True]

def get_active_todos(todos : list = None) -> list:
    if todos is None:
        todos = get_data()

    return [todo for todo in todos if todo['status'] == 'active']
