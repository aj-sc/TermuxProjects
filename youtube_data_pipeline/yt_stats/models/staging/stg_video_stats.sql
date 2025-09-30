with base_data as (
	select
	video_id,
	video_title,
	left(published_date::text, 10)::date as published_date,
	(
	coalesce((regexp_match(duration, 'PT(\d+)H'::text))[1], '0')::int * 3600
	+ coalesce((regexp_match(duration, '(\d+)M'::text))[1], '0')::int * 60
	+ coalesce((regexp_match(duration, '(\d+)S'::text))[1], '0')::int
        ) as duration_secs, 
	coalesce(nullif(views, '')::int, 0) as views,
	coalesce(nullif(likes, '')::int, 0) as likes,
	coalesce(nullif(comments, '')::int, 0) as comments,
	coalesce(nullif(favorites, '')::int, 0) as favorites
	from {{ source('raw', 'raw_video_stats') }}
),

data_rank as (
	select
	*,
	row_number() over (partition by video_id order by published_date desc) as dupe_check
	from base_data
)

select * from data_rank where dupe_check = 1

