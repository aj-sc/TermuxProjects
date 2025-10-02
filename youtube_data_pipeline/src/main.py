from extract.fetch_data import get_video_stats, get_video_ids, save_file
from load.load_data import read_file, get_connection, create_objects, insert_data, check_records

def main() -> None:
    # Fetch YouTube API and save results as JSON
    
    video_ids = get_video_ids()
    videos_info = get_video_stats()
    save_file(videos_info)

    # Read latest JSON file
    file_content = read_file()

    # Create schema and base table
    create_objects()

    # Insert data into table and check number of records added
    insert_data(file_content)
    check_records()

if __name__ = '__main__':
    main()
