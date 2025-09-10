{{ config(materialized='table') }}

select
    year,
    metro_code,
    city,
    region,
    state,
    max(case when var_description = 'Total Population' then value end) as total_population,
    max(case when var_description = 'Median Household Income' then value end) as median_household_income
from  {{ ref('stg_census') }}
group by year, metro_code, city, region, state
order by city, year