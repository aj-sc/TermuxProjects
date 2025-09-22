import db_manager

def add_todo():
    print('-' * 30)
    print('ADD NEW TASK')
    print()

    task = input('Task title: ')
    print()

    if not task:
        print('Task cannot be empty')
        return

    if db_manager.add_todo(task):
        print('To-do added sucessfully')
    else:
        print('Failed to add to-do')

    print('-' * 30)

def update_todo():
    print('-' * 30)
    print('UPDATE TASK')
    print()

    try:
        todo_id = int(input('Enter to-do id to update'))
        print()

    except ValueError:
        print('Invalid id')
        return

    confirmation = int(input('Are you sure you want to update this to-do ?, [Y/N]')).lower()
    print()

    if confirmation == 'y':
        if db_manager.update_todo(todo_id):
            print('To-do updated successfully')
        else:
            print('Failed to upload to-do')
    else:
        print('Update canceled')

    print('-' * 30)

def delete_todo():
    print('-' * 30)
    print('DELETE TASK')
    print()

    try:
        todo_id = int(input('Enter to-do id to delete'))
        print()
    except ValueError:
        print('Invalid id')
        return

    confirmation = input('Are you sure you want to delete this to-do ?, [Y/N]').lower()
    print()

    if confirmation == 'y':
        if db_manager.delete_todo(todo_id):
            print('To-do deleted successfully')
        else:
            print('Failed to delete to-do')
    else:
        print('Delete canceled')

    print('-' * 30)

def list_active_todos():
    todos = db_manager.get_active_todos()

    print('-' * 30)
    print('CURRENT TASKS: ')
    print()

    for row, todo in enumerate(todos, start=1):
        print(f'[{row}] Task: {todo['task']}')
        print(f'    Created: {todo['created_at']}')
        print(f'    Status: {'Completed' if todo['is_done'] == True else 'Pending'}')
        print()

    print('-' * 30)

def list_completed_todos():
    todos = db_manager.get_completed_todos()

    print('-' * 30)
    print('COMPLETED TASKS: ')
    print()

    for row, todo in enumerate(todos, start=1):
        print(f'[{row}] Task: {todo['task']}')
        print(f'    Created: {todo['created_at']}')
        print()

    print('-' * 30)
