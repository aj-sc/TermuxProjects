from todo import Todo

class TodoOperations:
    def __init__(self, database):
        self.database = database

    def create_todo(self, todo_id, task, status, is_done created_at, completed
