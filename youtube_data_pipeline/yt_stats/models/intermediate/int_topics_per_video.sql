with video_info as (
    
    select
	video_id,
	unnest(video_topics) as topic_url
    from {{ ref('stg_youtube_project__video_info') }}

),

clean_topics as (

    select
	video_id,
	regexp_replace(
		topic_url,
		'.*wiki/',
		''
	) as topic_name
    from video_info

)

select * from clean_topics
