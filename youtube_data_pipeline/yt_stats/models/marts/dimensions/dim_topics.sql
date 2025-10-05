with topics as (

    select * from {{ ref('int_topics') }}

)

select * from topics
