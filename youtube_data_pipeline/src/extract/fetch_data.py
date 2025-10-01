import os
from pathlib import Path
import requests
import json
from datetime import date
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
BASE_URL = 'https://www.googleapis.com/youtube/v3'

def get_video_stats(
        video_id: list, 
        api_key: str = API_KEY, 
        url: str = BASE_URL
        ) -> list:
    '''
    Retrieves statistics and metadata for one or more YouTube videos.

    Sends a request to the YouTube data API in batches of up to 50 videos IDs per request, and collect statistics and other information.

    Parameters:
    -----------
    - video_id (list[str]): A list of YouTube video IDs to fetch data for.
    - api_key (str, optional): YouTube data API key. Defaults to the global constant 'API KEY'.
    - url (str, optional): Base API url. Defaults to the global constant 'BASE URL'.

    Returns:
    --------
    - list[dict]: A list of dictionaries, where each dictionary contains:
        - video_id (str): Unique identifier of video.
        - video_title (str): Title of the video.
        - published_date (str): ISO 8601 date string when the video was published.
        - duration (str): Video duration in ISO 8601 format (example: 'PT15M33S').
        - likes (str): Number of likes.
        - views (str): Number of views.
        - comments (str): Number of comments.
        - favorites (str): Number of favorites.
        - video_topics (list[str]): A list of Wikipedia URLs that provide a high-level description of the video's content.
    '''
    custom_url = f'{url}/videos'
    video_stats_list = []
    
    for i in range(0, len(video_id), 50):
        batch = video_id[i:i+50]
        id_string = ','.join(batch)

        params = {
            'key' : api_key,
            'id' : id_string,
            'part' : 'statistics,contentDetails,snippet,topicDetails'
            }

        try:
            response = requests.get(custom_url, params=params)
            response.raise_for_status()

            data = response.json()
            
            items = data.get('items', [])

            for video in items:
                video_stats_list.append(
                    {
                        'video_id' : video.get('id', ''),
                        'video_title' : video.get('snippet', {}).get('title', ''),
                        'published_date' : video.get('snippet', {}).get('publishedAt', ''),
                        'duration' : video.get('contentDetails', {}).get('duration', ''),
                        'likes' : video.get('statistics', {}).get('likeCount', ''),
                        'views' : video.get('statistics', {}).get('viewCount', ''),
                        'comments' : video.get('statistics', {}).get('commentCount', ''),
                        'favorites' : video.get('statistics', {}).get('favoriteCount', ''),
                        'video_topics' : video.get('topicDetails', {}).get('topicCategories', [])
                    }
                )
        except requests.exceptions.HTTPError as err_h:
            print('Http Error: ', err_h)

    return video_stats_list

def get_video_ids(
        api_key: str = API_KEY, 
        channel_id: str = CHANNEL_ID, 
        url: str = BASE_URL
        ) -> list[str]:
    '''
    Fetch all video IDs from a given YouTube channel using the YouTube API v3.

    The function paginates throught the channel's upload, collecting all video IDs by looping page over page until no more pages are available.

    Parameters:
    -----------
    - api_key (str, optional): YouTube API key. Defaults to 'API_KEY' constant.
    - channel_id (str, optional): The YouTube channel ID. Defaults to 'CHANNEL_ID' constant.
    - url (str, optional): Base url of the YouTube API. Defaults to 'BASE_URL' constant.

    Returns:
    --------
    - list[str]: A list of YouTube video IDs that belong to the specified channel.
    '''
    custom_url = f'{url}/search'

    video_ids_list = []
    page_token = ''
    
    while True:
        params = {
            'key' : api_key,
            'channelId' : channel_id,
            'part' : 'snippet',
            'maxResults' : 50,
            'order' : 'date',
            'pageToken' : ''
            }
        
        if page_token:
            params["pageToken"] = page_token
        
        try:
            response = requests.get(custom_url, params=params)
            response.raise_for_status()

            data = response.json()
            items = data.get('items', [])
            
            video_ids_list.extend([
                item.get("id", {}).get("videoId", "")
                for item in items
                if item.get("id", {}).get("kind", "") == "youtube#video"
            ])
            
            page_token = data.get("nextPageToken", "")
            if not page_token:
                break
            
        except requests.exceptions.HTTPError as err_h:
            print(f'Request error: {err_h}')
        except requests.exceptions.RequestException as err_r:
            print(f'Request error: {err_r}')
    
    return video_ids_list

def save_file(data) -> None:
    '''
    Save data as a JSON file in the project 'data' folder with today's date.

    Parameters:
    -----------
    - data (list[dict]): The data to be serialized and saved in JSON format.

    Returns:
    --------
    None
    '''

    today = date.today()
    
    root_dir = Path(__file__).resolve().parents[2]
    data_dir = root_dir/'data'
    file_path = data_dir/f'video_data-{today}.json'
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print('File saved successfully!')

def main() -> None:
    video_ids = get_video_ids()
    video_stats_list = get_video_stats(video_ids)
    
    save_file(video_stats_list)
        
if __name__ == '__main__':
    main()
