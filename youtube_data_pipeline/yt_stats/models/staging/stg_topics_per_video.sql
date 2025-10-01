with base_data as (
	select
	video_id,
	video_topics,
	left(published_date::text, 10)::date as published_date
	from {{ source('raw', 'raw_video_stats') }}
),
set_dupe_check as (
	select
	*,
	row_number() over (partition by video_id order by published_date desc) as dupe_check
	from base_data
),
delete_dupes as (
	select
	*
	from set_dupe_check
	where dupe_check = 1
),
unnested_topics as (
	select
	video_id,
	unnest(video_topics) as topic_url
	from delete_dupes
),
cleaned_topics as (
	select
	video_id,
	regexp_replace(
		topic_url,
		'.*wiki/',
		''
	) as topic_name
	from unnested_topics
)

select * from cleaned_topics
