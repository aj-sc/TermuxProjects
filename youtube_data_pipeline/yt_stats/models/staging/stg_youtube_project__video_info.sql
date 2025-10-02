with source as (

	select * from {{ source('raw', 'raw_video_info') }}

),

cleaned as (
    select
	-- identifier
	video_id,

	-- strings
	video_title,

	-- dates
	published_date::timestamptz as published_at,

	-- numerics
	(coalesce((regexp_match(duration, 'PT(\d+)H'::text))[1], '0')::int * 3600
	+ coalesce((regexp_match(duration, '(\d+)M'::text))[1], '0')::int * 60
	+ coalesce((regexp_match(duration, '(\d+)S'::text))[1], '0')::int) as duration_secs, 
	coalesce(nullif(views, '')::int, 0) as views,
	coalesce(nullif(likes, '')::int, 0) as likes,
	coalesce(nullif(comments, '')::int, 0) as comments,
	coalesce(nullif(favorites, '')::int, 0) as favorites,

	-- arrays
	video_topics

    from source
),

final as (

    select
	*,
	row_number() over (partition by video_id order by published_at) as rn
    from cleaned

)

select * from final where rn = 1

