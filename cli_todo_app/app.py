from utils import ConsoleUtils

class App:

    def __init__(self, handler):
        self.handler = handler
    
    def main_menu(self):
        print('-' * 30)
        print('Main Menu\n')
        print('0 - Clear console')
        print('1 - Add to-do')
        print('2 - Complete to-do')
        print('3 - Delete to-do')
        print('4 - Show active to-dos')
        print('5 - Show completed to-dos')
        print('6 - Summary')
        print('7 - Delete all to-dos')
        print('8 - Exit app')
        print('-' * 30)
    
    def add_todo(self):
        ConsoleUtils.clear_console()
        
        print('-' * 30)
        print('ADD NEW TO-DO\n')
        
        task = input('Task title: ')

        if not task:
            print('Task cannot be empty')
            return
        
        if self.handler.add_todo(task):
            print('To-do added sucessfully')
        else:
            print('Failed to add to-do')

        print('-' * 30)
        
    def complete_todo(self):
        ConsoleUtils.clear_console()
        self.list_pending_todos()
        
        try:
            todo_index = int(input('Enter the number of the to-do you want to complete: '))
            print()

        except ValueError:
            print('Invalid number')
            return

        confirmation = input('Are you sure you want to complete this to-do ?, [Y/N]: ').lower()
        print()

        if confirmation == 'y':
            if self.handler.complete_todo(todo_index):
                print('To-do completed successfully')
            else:
                print('Failed to complete to-do')
        else:
            print('Operation canceled')

        print('-' * 30)
        
    def delete_todo(self):
        ConsoleUtils.clear_console()
        self.list_active_todos()
        
        try:
            todo_index = int(input('Enter the number of the to-do you want to delete: '))
            print()

        except ValueError:
            print('Invalid number')
            return

        confirmation = input('Are you sure you want to delete this to-do ?, [Y/N]: ').lower()
        print()

        if confirmation == 'y':
            if self.handler.delete_todo(todo_index):
                print('To-do deleted successfully')
            else:
                print('Failed to delete to-do')
        else:
            print('Operation canceled')

        print('-' * 30)
    
    def list_active_todos(self):
        ConsoleUtils.clear_console()
        
        active_todos = self.handler.get_active_todos()

        print('-' * 30)
        if active_todos:
            print('CURRENT TASKS\n')
            for i, todo in enumerate(active_todos, start=1):
                print(f"[{i}] Task: {todo['task']}")
                print(f"    Status: {'Completed' if todo['is_done'] else 'Pending'}")
                print(f"    Created: {todo['created_at']}")
                if todo['completed_at']:
                    print(f"    Completed: {todo['completed_at']}")
                print()
        else:
            print('No active tasks. Try adding some to-dos first!')
        print('-' * 30)
        
    def list_pending_todos(self):
        ConsoleUtils.clear_console()
        
        pending_todos = self.handler.get_pending_todos()

        print('-' * 30)
        if pending_todos:
            print('CURRENT TASKS\n')
            for i, todo in enumerate(pending_todos, start=1):
                print(f"[{i}] Task: {todo['task']}")
                print(f"    Created: {todo['created_at']}")
                print()
        else:
            print('There are no pending tasks available!')
        print('-' * 30)
    
    def list_completed_todos(self):
        ConsoleUtils.clear_console()
        
        completed_todos = self.handler.get_completed_todos()

        print('-' * 30)
        if completed_todos:
            print('CURRENT TASKS\n')
            for i, todo in enumerate(completed_todos, start=1):
                print(f"[{i}] Task: {todo['task']}")
                print(f"    Created: {todo['created_at']}")
                print(f"    Completed: {todo['completed_at']}")
                print()
        else:
            print('No tasks have been completed!')
        print('-' * 30)
    
    def summary(self):
        ConsoleUtils.clear_console()
        
        active_todos = len(self.handler.get_active_todos())
        completed_todos = len(self.handler.get_completed_todos(active_todos))
        completed_perc = round(completed_todos/active_todos, 2) if active_todos else 'No active to-dos available'
        
        print('-' * 30)
        print('SUMMARY\n')

        print(f'Total to-dos: {active_todos}')
        print(f'Completed to-dos: {completed_todos}\n')
        if active_todos:
            print(f'You have completed {completed_perc}% of your total to-dos.')

        print('-' * 30)
        
    def wipe_todos(self):
        ConsoleUtils.clear_console()
        
        active_todos = self.handler.get_active_todos()
        
        print('-' * 30)
        
        if active_todos:
            print('DELETE ALL TO-DOS\n')
            
            confirmation = input('Are you sure you want to delete all to-dos ?, [Y/N]: ').lower()
            print()

            if confirmation == 'y':
                self.handler.wipe_all_todos()
                print('All to-dos were deleted')
            else:
                print('Operation canceled')
    
        else:
            print('The database is empty, what about adding some to-dos first ?')
        
        print('-' * 30)
    
    def run(self):
        while True:
            self.main_menu()

            choice = int(input('Select an option: '))

            match choice:
                case 0:
                    ConsoleUtils.clear_console()
                case 1:
                    self.add_todo()
                case 2:
                    self.complete_todo()
                case 3:
                    self.delete_todo()
                case 4:
                    self.list_active_todos()
                case 5:
                    self.list_completed_todos()
                case 6:
                    self.summary()
                case 7:
                    self.wipe_todos()
                case 8:
                    ConsoleUtils.exit_app()

            input('Press Enter to continue...')