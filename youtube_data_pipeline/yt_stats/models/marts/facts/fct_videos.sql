with video_info as (

    select * from {{ ref('stg_youtube_project__video_info') }}

),

bridge_video_topics as (

    select * from {{ ref('int_bridge_video_topics') }}

),

topics as (

    select * from {{ ref('dim_topics') }}

),

final as (

    select
	v.video_id,
	video_title,
	v.published_at,
	v.duration_secs,
	v.likes,
	v.views,
	v.comments,
	v.favorites,
	t.topic_id
    from video_info as v
    left join bridge_video_topics as b
	on v.video_id = b.video_id
    left join topics as t
	on b.topic_id = t.topic_id

)

select * from final
