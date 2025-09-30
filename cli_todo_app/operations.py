from db_manager import get_data, db_add_todo, db_complete_todo, db_delete_todo, get_active_todos, get_completed_todos

def add_todo() -> None:
    '''
    Prompt the user to add a new to-do and store it in the database. It calls db_add_todo from db_manager to perform the write operation.

    Returns:
    --------
    - None, this function does not return anything. It only prints messages indicating success or failure.
    '''

    print('-' * 30)
    print('ADD NEW TASK')
    print()

    task = input('Task title: ')
    print()

    if not task:
        print('Task cannot be empty')
        return

    if db_add_todo(task):
        print('To-do added sucessfully')
    else:
        print('Failed to add to-do')

    print('-' * 30)

def complete_todo() -> None:
    '''
    Prints a list of active to-dos and then it prompts the user to select the to-do to complete. It calls list_active_todos and db_complete_todo from db_manager to perform the update status operation.

    Returns:
    --------
    - None, this function does not return anything, it only prints messages indicating success or failure.
    '''

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
        if db_complete_todo(todo_index):
            print('To-do completed successfully')
        else:
            print('Failed to complete to-do')
    else:
        print('Operation canceled')

    print('-' * 30)

def delete_todo() -> None:
    '''
    Prints a list of active to-dos and then it prompts the user to select the to-do to delete. It calls list_active_todos and db_delete_todo from db_manager to perform the update status operation.

    Returns:
    --------
    - None, this function does not return anything, it only prints messages indicating success or failure.
    '''

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
        if db_delete_todo(todo_index):
            print('To-do deleted successfully')
        else:
            print('Failed to delete to-do')
    else:
        print('Operation canceled')

    print('-' * 30)

def list_active_todos() -> None:
    '''
    Prints a list of active to-dos. It calls get_active_todos() from db_manager to get the to-do data.

    Returns:
    --------
    - None, this function does not return anything, it only prints messages indicating success or failure.
    '''

    todos = get_data()
    active_todos = get_active_todos(todos)

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

def list_completed_todos() -> None:
    '''
    Prints a list of active completed to-dos. It calls get_completed_todos() from db_manager to get the to-do data.

    Returns:
    --------
    - None, this function does not return anything, it only prints messages indicating success or failure.
    '''

    todos = get_data()
    completed_todos = get_completed_todos(todos)

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
    '''
    Displays analytics for the current to-do list. It calls get_data(), get_active_todos() and get_completed_todos() from db_manager to calculate the corresponding metrics.

    Returns:
    --------
    - None, this function does not return anything, it prints the analytics directly to the console.
    '''

    todos = get_data()
    active_todos = len(get_active_todos(todos))
    completed_todos = len(get_completed_todos(todos))
    complete_perc = round((completed_todos/active_todos) * 100, 2)

    print('-' * 30)
    print('ANALYTICS')
    print()

    print(f'Total to-dos: {active_todos}')
    print(f'Completed to-dos: {completed_todos}')
    print()
    print(f'You have completed {complete_perc}% of your total to-dos.')

    print('-' * 30)


