from datetime import datetime

class Todo:
    def __init__(
            self, 
            todo_id, 
            task, 
            status = 'active', 
            is_done = False, 
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
            completed_at = None
        ):
        self.todo_id = todo_id
        self.task = task
        self.status = status
        self.is_done = is_done
        self.created_at = created_at
        self.completed_at = completed_at

    def to_dict(self):
        return {
            'todo_id' : self.todo_id,
            'task' : self.task,
            'status' : self.status,
            'is_done' : self.is_done,
            'created_at' : self.created_at,
            'completed_at' : self.completed_at
        }
        
