import psycopg2
import json
import os
from psycopg2.extras import execute_values
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR/'data'

def read_file():
    latest_file = max(DATA_DIR.glob('*.json'), key=lambda f: f.stat().st_mtime)

    with open(latest_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def get_connection():
    db_params = {
        'host' : 'localhost',
        'database' : 'youtube_project',
        'user' : os.getenv('DB_USER'),
        'password' : os.getenv('DB_PASSWORD'),
        'port' : '5432'
        }

    try:
        conn = psycopg2.connect(**db_params)

        return conn
    except psycopg2.Error as err:
        print(f'Failed to connect: {err}')

def create_objects() -> None:
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute('''
                    DROP SCHEMA IF EXISTS raw CASCADE;
                    CREATE SCHEMA raw;
                    CREATE TABLE raw.raw_video_info (
                        id serial PRIMARY KEY,
                        video_id TEXT NOT NULL,
                        video_title TEXT NOT NULL,
                        published_date TIMESTAMPTZ NOT NULL,
                        duration TEXT NOT NULL,
                        likes TEXT NOT NULL,
                        views TEXT NOT NULL,
                        comments TEXT NOT NULL,
                        favorites TEXT NOT NULL,
                        video_topics TEXT[][] NOT NULL
                    );''')
    
        print('Success, raw schema and raw_video_info table created')
    except psycopg2.Error as err:
        print(f'Failed to create objects: {err}')

def insert_data(data : list) -> None:
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                rows = [(v['video_id'], v['video_title'], v['published_date'], v['duration'], v['likes'], v['views'], v['comments'], v['favorites'], v['video_topics']) for v in data]

                execute_values(
                    curr, 'INSERT INTO raw.raw_video_info (video_id, video_title, published_date, duration, likes, views, comments, favorites, video_topics) VALUES %s', rows)
        
        print('Success, data inserted into table')
    except psycopg2.Error as err:
        print(f'Failed to insert data: {err}')

def check_records():
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute('''
                    SELECT count(*) AS total_videos, count(distinct video_id) as unique_videos FROM raw.raw_video_info;''')

                data = curr.fetchone()
                
        print(f'Success, {data[0]} total records vs {data[1]} unique records')
    except psycopg2.Error as err:
        print(f'Failed to retreive records: {err}')

def main() -> None:
    try:
        # Get data from the latest json file
        file_content = read_file()

        # Create schema and table
        create_objects()

        # Insert data into schema table
        insert_data(file_content)

        # Check number of records added
        check_records()
    except Exception as e:
        print(f'Failed to run proccess: {e}')

if __name__ == '__main__':
    main()
