{{ config(materialized='table') }}

with income as (
    select
        year,
        city,
        value as median_household_income
    from {{ ref('stg_census') }}
    where var_code = 'B19013_001E'
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
    i.year,
    i.city,
    i.median_household_income,
    p.home_price_index,
    safe_divide(i.median_household_income, p.home_price_index) as income_to_price_ratio
from income i
left join prices p on i.year = p.year and i.city = p.city