from todo import Todo
from datetime import datetime

class Handler:
    def __init__(self, database):
        self.database = database
    
    # Filter operations
        
    def get_active_todos(self, data = None):
        if data is None:
            data = self.database.read_database()
            
        return [item for item in data if item['status'] == 'active']
    
    def get_pending_todos(self, data = None):
        if data is None:
            data = self.database.read_database()
            
        return [item for item in data if item['status'] == 'active' and item['is_done'] == False]
    
    def get_completed_todos(self, data = None):
        if data is None:
            data = self.database.read_database()
            
        return [item for item in data if item['status'] == 'active' and item['is_done'] == True]
    
    # CRUD operations
    
    def add_todo(self, task: str):
        try:
            records = self.database.read_database()

            new_id = max(todo.get('todo_id', 0) for todo in records) + 1 if records else 1
                
            todo = Todo(
                todo_id=new_id,
                task=task,
                status='active',
                is_done=False,
                created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                completed_at=None
            )

            records.append(todo.to_dict())

            if self.database.write_to_database(records):
                return True
        
        except Exception as e:
            print('Error: ', e)
            return False

        print(f"✅ Todo '{task}' added successfully with ID {new_id}")
        
    def complete_todo(self, todo_position : int):
        try:
            todos = self.database.read_database()
            pending_todos = self.get_pending_todos(todos)
            
            pending_todos[todo_position - 1]['is_done'] = True
            pending_todos[todo_position - 1]['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if self.database.write_to_database(todos):
                return True
            
        except Exception as e:
            print('Error: ', e)
            return False
    
    def delete_todo(self, todo_position : int):
        try:
            todos = self.database.read_database()
            active_todos = self.get_active_todos(todos)
            
            active_todos[todo_position - 1]['status'] = 'inactive'

            if self.database.write_to_database(todos):
                return True
            
        except Exception as e:
            print('Error: ', e)
            return False
    
    def wipe_all_todos(self):
        self.database.write_to_database([])
        
