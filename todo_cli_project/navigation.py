import os
from operations import add_todo, list_completed_todos, list_active_todos

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_main_menu():
    print('-' * 30)
    print('Main Menu')
    print()
    print('0 - Clear console')
    print('1 - Add to-do')
    print('2 - Update to-do')
    print('3 - Delete to-do')
    print('4 - Show active to-dos')
    print('5 - Show completed to-dos')
    print('6 - Exit app')
    print('-' * 30)

def navigation():

    while True:
        show_main_menu()

        choice = int(input('Select an option: '))

        match choice:
            case 0:
                clear_console()
            case 1:
                add_todo()
            case 2:
                update_todo()
            case 3:
                delete_todo()
            case 4:
                list_active_todos()
            case 5:
                list_completed_todos()
            case 6:
                break

        input('Press Enter to continue...')

navigation()


