import json
import os

title = input('Write the title: ')
body = input('Write the body: ')

def add_note(note_title, note_body):
    note = {
        'title' : note_title,
        'body' : note_body
        }

    if not os.path.isfile('notes_db.json'):
        with open('notes_db.json', 'w') as file:
            json.dump(note, file, indent=4)
            print('db created')

add_note(title, body)
