-- tpv aka topics per video
with tpv as (
	select
	*
	from {{ ref('stg_topics_per_video') }}
),
bridge_table as (
	select
	tpv.video_id,
	vt.topic_id
	from tpv
	join {{ ref('stg_video_topics') }} as vt
	on vt.topic_name = tpv.topic_name
)

select * from bridge_table
