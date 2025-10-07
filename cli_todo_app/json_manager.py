import json
from pathlib import Path

class JsonManager:
    FILE_PATH = Path('database.json')

    def __init__(self, db_path = FILE_PATH):
        self.db_path = db_path

        if not db_path.exists():
            with open(db_path, 'w') as file:
                json.dump([], file, indent=4, ensure_ascii=False)

    # Base operations

    def read_database(self):
        with open(self.db_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def write_to_database(self, data):
        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
        return True