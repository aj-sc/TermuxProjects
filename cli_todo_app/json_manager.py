import json
from datetime import datetime
from pathlib import Path

class JsonManager:
    FILE_PATH = 'database.json'

    def __init__(self, db_path = FILE_PATH):
        self.db_path = db_path

        if not db_path.exists():
            with open(db_path, 'w') as file:
                json.dump([], file, indent=4)

    # Base operations

    def read_database(self):
        with open(self.db_path, 'r') as file:
            data = json.load(file)

        return data

    def write_to_database(self, data):
        with open(self.db_path, 'w') as file:
            json.dump(data, file, indent=4)

    # Get data methods

    def get_active_records(self, data = None):
        if data is None:
            data = self.read_database()

        return [item for item in data if item['status'] == 'active']

    def get_pending_records(self, data = None):
        if data is None:
            data = self.read_database()

        return [item for item in data if item['is_done'] == False and item['status'] == 'active']
    
    def get_completed_records(self, data = None):
        if data is None:
            data = self.read_database()

        return [item for item in data if item['is_done'] == True and item['status'] == 'active']

    # CRUD operations

    def add_record(self, new_record):
        records = self.read_database()
        records.append(new_record)
        self.write_to_database(records)

    def complete_record(self, record_id):
        records = self.read_database()
        pending_records = self.get_pending_records(records)

        pending_records[record_id - 1]['is_done'] = True
        pending_records[record_id - 1]['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.write_to_database(records)

    def delete_record(self, record_id):
        records = self.read_database()
        active_records = self.get_active_records(records)

        active_records[record_id - 1]['status'] = 'inactive'

        self.write_to_database(records)
