import sqlite3

def get_connection():
    conn = sqlite3.connect('data/youtube.db')
    conn.row_factory = sqlite3.Row  # access rows like dicts
    
    return conn

with get_connection() as conn:
    cursor = conn.cursor()
    
    data = cursor.execute('SELECT * FROM videos_data LIMIT 50;').fetchall()
    
for row in data:
    print(dict(row))

