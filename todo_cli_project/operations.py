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

def complete_todo():
    list_active_todos()

    try:
        todo_index = int(input('Enter the number of the to-do you want to complete: '))
        print()

    except ValueError:
        print('Invalid number')
        return

    confirmation = input('Are you sure you want to complete this to-do ?, [Y/N]: ').lower()
    print()

    if confirmation == 'y':
        if db_manager.complete_todo(todo_index):
            print('To-do completed successfully')
        else:
            print('Failed to complete to-do')
    else:
        print('Operation canceled')

    print('-' * 30)

def delete_todo():
    list_active_todos()

    try:
        todo_index = int(input('Enter the number of the to-do you want to delete: '))
        print()
    except ValueError:
        print('Invalid number')
        return

    confirmation = input('Are you sure you want to delete this to-do ?, [Y/N]: ').lower()
    print()

    if confirmation == 'y':
        if db_manager.delete_todo(todo_index):
            print('To-do deleted successfully')
        else:
            print('Failed to delete to-do')
    else:
        print('Operation canceled')

    print('-' * 30)

def list_active_todos():
    todos = db_manager.get_data()
    active_todos = db_manager.get_active_todos(todos)

    print('-' * 30)
    print('CURRENT TASKS')
    print()

    for row, todo in enumerate(active_todos, start=1):
        print(f'[{row}] Task: {todo['task']}')
        print(f'    Status: {'Completed' if todo['is_done'] == True else 'Pending'}')
        print(f'    Created: {todo['created_at']}')
        if todo['completed_at'] is not None:
            print(f'    Completed: {todo['completed_at']}')
        print()

    print('-' * 30)

def list_completed_todos():
    todos = db_manager.get_data()
    completed_todos = db_manager.get_completed_todos(todos)

    print('-' * 30)
    print('COMPLETED TASKS')
    print()

    for row, todo in enumerate(completed_todos, start=1):
        print(f'[{row}] Task: {todo['task']}')
        print(f'    Created: {todo['created_at']}')
        print(f'    Completed: {todo['completed_at']}')
        print()

    print('-' * 30)

def analytics():
    todos = db_manager.get_data()
    active_todos = len(db_manager.get_active_todos(todos))
    completed_todos = len(db_manager.get_completed_todos(todos))
    complete_perc = round((completed_todos/active_todos) * 100, 2)

    print('-' * 30)
    print('ANALYTICS')
    print()

    print(f'Total to-dos: {active_todos}')
    print(f'Completed to-dos: {completed_todos}')
    print()
    print(f'You have completed {complete_perc}% of your total to-dos.')

    print('-' * 30)


