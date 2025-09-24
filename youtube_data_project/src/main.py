import json
from operations import get_video_ids, get_video_stats

def main() -> None:
    video_ids = get_video_ids()
    video_stats_list = get_video_stats(video_ids)

    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(video_stats_list, f, indent=4, ensure_ascii=False)