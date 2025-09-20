import json

def get_db() -> list:
    try:
        with open('database.json', 'r') as file:
            data = json.load(file)

        return data
    except FileNotFoundError:
        data = []
        with open('database.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        return data

def add_note(data : list, title : str, body :str) -> None:
    note_id = data[-1].get('note_id', '') + 1 if data else 1
    new_note = {
            'note_id' : note_id,
            'note_title' : title,
            'note_body' : body,
            'note_status' : 'active'
            }

    data.append(new_note)

    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)

def update_note():
    pass

def delete_notes():
    pass

def list_active_notes(data : list):
    for note in data:
        if note['note_status'] == 'active':
            print('')
            print(f'- Title: {note['note_title']}')
            print(f'- Description: {note['note_body']}')
            print('')
