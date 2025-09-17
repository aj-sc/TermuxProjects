import json

title = input('Write the title: ')
body = input('Write the body: ')

def get_notes() -> list:
    with open('notes_db.json', 'r') as file:
        data = json.load(file)

    if not data:
        return []

    return data

def add_note(note_title, note_body) -> None:
    notes_data = get_notes()

    note_id = notes_data[-1]['id'] + 1 if notes_data else 1

    note = {
        'id' : note_id,
        'title' : note_title,
        'body' : note_body
        }

    notes_data.append(note)

    with open('notes_db.json', 'w') as file:
        json.dump(notes_data, file, indent=4)
        print('Note added to db')

def main() -> None:
    pass

if __name__ == '__main__':
    main()
