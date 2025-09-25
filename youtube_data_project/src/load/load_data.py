import sqlite3
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR/'data'

def read_file():
    latest_file = max(DATA_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime)
    
    with open(latest_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

def get_connection():
    conn = sqlite3.connect(DATA_DIR/'raw.db')
    conn.row_factory = sqlite3.Row  # access rows like dicts
    
    return conn

def innit_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS raw_video_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                video_id TEXT UNIQUE NOT NULL,
                video_title TEXT NOT NULL,
                published_date TEXT NOT NULL,
                duration TEXT NOT NULL,
                likes TEXT NOT NULL,
                views TEXT NOT NULL,
                comments TEXT NOT NULL,
                favorites TEXT NOT NULL
            );
        '''
        )
        
    print('Success: videos_data table created')
    
def insert_videos(data : list):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.executemany('''
            INSERT OR REPLACE INTO raw_video_stats (video_id, video_title, published_date, duration, likes, views, comments, favorites)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);''',
            [(v['video_id'], v['video_title'], v['published_date'], v['duration'], v['likes'], v['views'], v['comments'], v['favorites']) 
            for v in data]
        )
    
    print('Success: Data inserted into table')
    
def main():
    # Get file data
    file_content = read_file()
    # Create table
    innit_db()
    # Insert data to db
    insert_videos(file_content)

if __name__ == '__main__':
    main()
