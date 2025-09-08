with source as (
    select * from {{ source('raw', 'fred_rates') }}
),

cleaned as (
    select
        date,
        extract(year from date) as year,
        series_id,
        value,
        rate_type
    from source
),

mapped as (
    select
        c.date,
        c.year,
        c.series_id,
        c.value,
        fr.indicator as rate_name
    from cleaned c
    left join {{ ref('fred_rates') }} fr on c.series_id = fr.series_id
)

select * from mapped