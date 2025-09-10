{{ config(materialized='table') }}

with population as (
    select
        year,
        city,
        value as population
    from {{ ref('stg_census') }}
    where var_code = 'B01003_001E'
),
prices as (
    select
        year,
        city,
        value as home_price_index
    from {{ ref('stg_fred_metros') }}
    where indicator = 'Case_Shiller_Home_Price_Index'
)
select
    p.year, 
    p.city,
    pop.population,
    p.home_price_index,
    safe_divide(p.home_price_index, pop.population) as price_per_capita
from prices p
left join population pop on p.year = pop.year and p.city = pop.city