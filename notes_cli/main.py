import json

note_title = input('Write the title: ')
note_body = input('Write the body: ')

note = {
    'title' : note_title,
    'body' : note_body
    }

data = json.dumps(note, indent=4)

print(data)
