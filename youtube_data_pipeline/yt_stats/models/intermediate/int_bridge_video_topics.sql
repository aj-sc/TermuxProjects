with video_info as (

    select * from {{ ref('stg_youtube_project__video_info') }}

),

topics as (

    select * from {{ ref('int_topics') }}

),

topics_per_video as (

    select * from {{ ref('int_topics_per_video') }}

),

topics_per_video_enriched as (

    select
	tv.video_id,
	tv.topic_name,
	t.topic_id
    from topics_per_video as tv
    join topics as t
    	on t.topic_name = tv.topic_name

),

final as (

    select
	video_id,
	topic_id
    from topics_per_video_enriched

)

select * from final
