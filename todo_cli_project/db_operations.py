import json
from datetime import date

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

def add_todo(data : list, task : str) -> None:
    todo_id = data[-1].get('todo_id', 0) + 1 if data else 1
    new_todo = {
            'todo_id' : todo_id,
            'task' : task,
            'status' : 'active',
            'is_done' : False,
            'created_at' : str( date.today())
            }

    data.append(new_todo)

    write_data(data)

def update_todo(todo_id : int) -> None:
    todos = get_data()

    todos[todo_id - 1]['is_done'] = True
    
    write_data(todos)

def delete_todo(todo_id : int) -> None:
    todos = get_data()

    todos[todo_id - 1]['status'] = 'inactive'

    write_data(todos)

def list_completed_todos(data : list) -> None:
    if len([todo for todo in data if todo['is_done'] == True]) > 0:
        print('Completed to-dos:')
        for todo_id, todo in enumerate(data, start=1):
            if todo['is_done'] == True:
                print(f'{todo_id} - {todo['task']}')
    else:
        print('No completed to-dos')


def list_active_todos(data : list) -> None:
    print('Active to-dos')
    active_todos = [todo for todo in data if todo['status'] == 'active']
    for todo_id, todo in enumerate(active_todos, start=1):
        print(f'{todo_id} - {todo['task']}')
