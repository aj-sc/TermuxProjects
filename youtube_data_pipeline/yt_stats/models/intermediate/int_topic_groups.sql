with video_info as (

    select * from {{ ref('stg_youtube_project__video_info') }}

),

remove_url_string_from_topics as (

    select
        regexp_replace(
            video_topics,
            '.*wiki/',
            ''
        ) as topic
    from video_info

),

deduplicate_topic_groups as (

    select distinct topic from remove_url_string_from_topics

),

final as (

    select
        row_number() over () as topic_id,
        topic as topic_name
    from deduplicate_topic_groups

)

select * from final