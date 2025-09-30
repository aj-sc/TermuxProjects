import os
import sys
from operations import add_todo, complete_todo, delete_todo, list_completed_todos, list_active_todos, analytics

def clear_console() -> None:
    '''
    Clears consolo output to improve user experience and readability. Uses appropiate command depending on the operating system: 'cls' for Windows and 'clear' for Linux/MacOS.

    Returns:
    --------
    - None
    '''

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_main_menu() -> None:
    '''
    Display the main menu and navigation options of the application.

    Returns:
    --------
    - None
    '''
    print('-' * 30)
    print('Main Menu')
    print()
    print('0 - Clear console')
    print('1 - Add to-do')
    print('2 - Complete to-do')
    print('3 - Delete to-do')
    print('4 - Show active to-dos')
    print('5 - Show completed to-dos')
    print('6 - Show analytics')
    print('7 - Exit app')
    print('-' * 30)
    
def exit_program() -> None:
    '''
    Prints separator line before exiting the application with a goodbye message.

    Returns:
    --------
    - None
    '''
    print('-' * 30)
    sys.exit('Goodbye!')

def navigation() -> None:
    '''
    Run the main navigation loop for the application. Displays main menu and show navigation options, calls all the necessary functions from operations.

    Returns:
    --------
    - None, this function does not return anything. It just controls the application flow via user input.
    '''

    while True:
        show_main_menu()

        choice = int(input('Select an option: '))

        match choice:
            case 0:
                clear_console()
            case 1:
                add_todo()
            case 2:
                complete_todo()
            case 3:
                delete_todo()
            case 4:
                list_active_todos()
            case 5:
                list_completed_todos()
            case 6:
                analytics()
            case 7:
                exit_program()

        input('Press Enter to continue...')
