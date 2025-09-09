with source as (
    select * from {{ source('raw', 'fred_metros') }}
),
cleaned as (
    select
        date,
        series_id,
        value,
        geo_id,
        extract(year from date) as year
    from source
    where geo_id is not null
),
mapped as (
    select 
        c.date,
        c.series_id,
        c.year,
        c.value,
        c.geo_id,
        initcap(replace(fm.metro, '_', ' ')) as city,
        initcap(fm.indicator) as indicator
    from cleaned c
    left join {{ ref('fred_metros') }} fm on c.series_id = fm.series_id
)
select 
    * 
from mapped