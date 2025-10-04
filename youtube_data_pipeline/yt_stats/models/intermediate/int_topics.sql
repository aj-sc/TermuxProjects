with video_info as (

    select * from {{ ref('stg_youtube_project__video_info') }}

),

unnested_topics as (

    select
	unnest(video_topics) as topic
    from video_info

),

clean_topics as (

    select
	regexp_replace(
		topic,
		'.*wiki/',
		''
	) as cleaned_topic
    from unnested_topics

),

deduplicate_topics as (

    select
	distinct cleaned_topic
    from clean_topics

),

final as (

    select
	row_number() over () as topic_id,
	cleaned_topic as topic_name
    from deduplicate_topics

)

select * from final
