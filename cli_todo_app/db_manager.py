import json
from datetime import datetime

FILE_PATH = 'database.json'

def write_data(
        data : list, 
        path : str = FILE_PATH
    ) -> None:
    '''
    Write data to JSON file.

    Parameters:
    -----------
    - data (list): A JSON list (list of dictionaries), that contains the to-dos you want to store.
    - path (str): Path to the file that serves as the database.
    '''
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def get_data(path : str = FILE_PATH) -> list:
    '''
    Read the current JSON file and return it's content.

    Parameters:
    -----------
    - path (str): Path to the file that serves as the database.

    Returns:
    --------
    - file_content or empty list (list): Reads the JSON file and returns it's content, if file does not exists if creates an empty one and returns an empty list.
    '''
    try:
        with open(path, 'r') as file:
            file_content = json.load(file)

        return file_content
    except FileNotFoundError:
        write_data([])

        return []

def db_add_todo(task : str) -> bool:
    '''
    Adds to-do to database.

    Parameters:
    -----------
    - task (str): Content of the to-do that you want to write to the database.

    Returns:
    -----------
    - True or False (bool): True if to-do was added successfully, false if any error ocurred.
    '''
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

def db_complete_todo(todo_index : int) -> bool:
    '''
    Changes to-do status from pending to completed.

    Parameters:
    -----------
    - todo_index (int): The position of the to-do in the list of active to-dos.

    Returns:
    --------
    - True or False (bool): True if to-do status was updated successfully, false if any error ocurred.
    '''
    try:
        todos = get_data()
        pending_todos = get_pending_todos(todos)

        pending_todos[todo_index - 1]['is_done'] = True
        pending_todos[todo_index - 1]['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        write_data(todos)

        return True
    except Exception as err:
        print('Error: ', err)
        return False

def db_delete_todo(todo_index : int) -> None:
    '''
    Changes to-do from active to inactive.

    Parameters:
    -----------
    - todo_index (int): The position of the to-do in the list of active to-dos.

    Returns:
    --------
    - True or False (bool): True if to-do active status was updated successfully, false if any error ocurred.
    '''
    try:
        todos = get_data()
        active_todos = get_active_todos(todos)

        active_todos[todo_index - 1]['status'] = 'inactive'

        write_data(todos)

        return True
    except Exception as err:
        print('Error: ', err)
        return False

def get_pending_todos(todos: list = None) -> list:
    '''
    Get a list of pending to-dos

    Parameters:
    -----------
    - todos (list, optional): List of all to-do items. If None, fetches from database.

    Returns:
    --------
    - list: A list of to-do items where 'is_done' is False.
    '''
    if todos is None:
        todos = get_data()

    return [todo for todo in todos if todo['is_done'] == False and todo['status'] == 'active']

def get_completed_todos(todos : list = None) -> list:
    '''
    Get a list of completed to-dos.

    Parameters:
    -----------
    - todos (list, optional): List of all to-do items. If None, fetches from database.

    Returns:
    --------
    - list: A list of to-do items where 'is_done' is True. 
    '''
    if todos is None:
        todos = get_data()

    return [todo for todo in todos if todo['is_done'] == True and todo['status'] == 'active']

def get_active_todos(todos : list = None) -> list:
    '''
    Get a list of active to-dos.

    Parameters:
    -----------
    - todos (list, optional): List of all to-do items. If None, fetches from database.

    Returns:
    --------
    - list: A list of to-do items where 'status' is active.
    '''
    if todos is None:
        todos = get_data()

    return [todo for todo in todos if todo['status'] == 'active']
