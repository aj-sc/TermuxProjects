with unnested_topics as (
	select
	unnest(video_topics) as topic_url
	from {{ source('raw', 'raw_video_stats') }}
),
with cleaned_topics as (
	select
	regexp_replace(
		topic_url,
		'.*wiki/',
		''
	) as topic_name
	from unnested_topics
),
final as (
	select
	distinct topic_name
	from cleaned_topics
)

select
row_number() over () as topic_id,
topic_name
from final
