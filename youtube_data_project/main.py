import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
BASE_URL = 'https://www.googleapis.com/youtube/v3'

def get_video_stats(video_id: list, api_key: str = API_KEY, url: str = BASE_URL) -> list:
    custom_url = f'{url}/videos'

    joined_ids = ','.join(video_id)

    params = {
         'key' : api_key,
         'id' : joined_ids,
         'part' : 'statistics,contentDetails,snippet'
        }

    video_stats_list = []

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
                        'favorites' : video.get('statistics', {}).get('favoriteCount', '')
                     }
                    )
    except requests.exceptions.HTTPError as err_h:
        print('Http Error: ', err_h)

    return video_stats_list

def get_video_ids(api_key: str = API_KEY, channel_id: str = CHANNEL_ID, url: str = BASE_URL) -> list | None:
    custom_url = f'{url}/search'

    params = {
        'key' : api_key,
        'channelId' : channel_id,
        'part' : 'snippet',
        'maxResults' : 50,
        'order' : 'date',
        'pageToken' : ''
        }

    video_ids_list = []

    try:
        response = requests.get(custom_url, params=params)
        response.raise_for_status()

        data = response.json()
        items = data.get('items', [])

        video_ids_list = [video.get('id', {}).get('videoId', '') for video in items if video.get('id', {}).get('kind', '') == 'youtube#video']

    except requests.exceptions.HTTPError as err_h:
        print('Http Error: ', err_h)
    
    return video_ids_list

def main() -> None:
    id_string = get_video_ids()
    video_list = get_video_stats(id_string)

    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(video_list, file, indent=4, ensure_ascii=False)
        print('Test file saved')

if __name__ == '__main__':
    main()
