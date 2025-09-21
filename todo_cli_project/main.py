from db_operations import get_data, add_todo, list_completed_todos, list_active_todos, delete_todo
import argparse

def main2() -> None:
    parser = argparse.ArgumentParser(description='Add and manage your to-dos')
    parser.add_argument('action', choices=['add', 'delete', 'pending', 'active'], help='Pick an option')

    args = parser.parse_args()

    match args.action:
        case 'add':
            pass
        case 'delete':
            pass
        case 'pending':
            pass
        case 'active':
            pass

def main() -> None:
    while True:
        print("""

Welcome to your home app, press the desired option:

1 - Add todo
2 - Show completed todos
3 - Show active todos
4 - Delete todo
5 - Exit app

""")

        nav_input = input("Choose an option: ")
        print()

        match int(nav_input):
            case 1:
                task = input("Write new task: ")

                todos = get_data()
                add_todo(todos, task)

            case 2:
                todos = get_data()
                list_completed_todos(todos)

            case 3:
                todos = get_data()
                list_active_todos(todos)

            case 4:
                todos = get_data()
                list_active_todos(todos)
                print()

                todo_id = int(input('Select the number of the to-do you want to delete: '))

                delete_todo(todo_id)

            case 5:
                print("Exiting app...")
                break

            case _:
                print("Invalid option, try again.")


if __name__ == "__main__":
    main()
