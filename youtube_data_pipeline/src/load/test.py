import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR/'data'

def get_connection():
    conn = sqlite3.connect(DATA_DIR/'raw.db')
    conn.row_factory = sqlite3.Row  # access rows like dicts
    
    return conn

with get_connection() as conn:
    cursor = conn.cursor()
    
    data = cursor.execute('select count(*) as total_records from raw_video_stats;').fetchone()
    count = data['total_records']

    print(f'Number of videos: {count}')

