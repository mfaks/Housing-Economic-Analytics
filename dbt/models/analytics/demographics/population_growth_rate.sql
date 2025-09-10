{{ config(materialized='table') }}

with base as (
    select
        year,
        metro_code,
        city, 
        region,
        state,
        max(case when var_description = 'Total Population' then value end) as total_population,
    FROM {{ ref('stg_census') }}
    GROUP BY year, metro_code, city, region, state
)

select
    year,
    metro_code,
    city,
    region, 
    state,
    total_population,
    safe_divide(
        total_population - lag(total_population) over (partition by metro_code order by year),
        lag(total_population) over (partition by metro_code order by year)
    ) as population_growth_rate
from base
order by city, year