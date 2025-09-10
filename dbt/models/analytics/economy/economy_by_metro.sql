{{ config(materialized='table') }}

select
    year,
    city,
    max(case when indicator = 'Case_Shiller_Home_Price_Index' then value end) as home_price_index,
    max(case when indicator = 'Consumer_Price_Index' then value end) as consumer_price_index,
    max(case when indicator = 'Unemployment_Rate' then value end) as unemployment_rate
from {{ ref('stg_fred_metros') }}
group by year, city
order by city, year