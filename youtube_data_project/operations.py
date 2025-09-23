import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
BASE_URL = 'https://www.googleapis.com/youtube/v3'

def get_video_stats(video_id: list, api_key: str = API_KEY, url: str = BASE_URL) -> list:
    custom_url = f'{url}/videos'
    video_stats_list = []
    
    for i in range(0, len(video_id), 50):
        batch = video_id[i:i+50]
        id_string = ','.join(batch)

        params = {
            'key' : api_key,
            'id' : id_string,
            'part' : 'statistics,contentDetails,snippet'
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
                        'likes' : video.get('statistics', {}).get('likeCount', 0),
                        'views' : video.get('statistics', {}).get('viewCount', 0),
                        'comments' : video.get('statistics', {}).get('commentCount', 0),
                        'favorites' : video.get('statistics', {}).get('favoriteCount', 0)
                    }
                )
        except requests.exceptions.HTTPError as err_h:
            print('Http Error: ', err_h)

    return video_stats_list

def get_video_ids(api_key: str = API_KEY, channel_id: str = CHANNEL_ID, url: str = BASE_URL) -> list | None:
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
