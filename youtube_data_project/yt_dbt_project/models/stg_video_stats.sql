{{ config(materialized='table', schema='staging') }}

select
row_number() over () as id,
cast(video_id as text) as video_id,
cast(video_title as text) as video_title,
date(replace(replace(published_date, 'T', ' '), 'Z', '')) as publish_date,
cast(duration as text) as duration,
cast(likes as integer) as likes,
cast(views as integer) as views,
cast(comments as integer) as comments,
cast(favorites as integer) as favorites
from raw_video_stats
