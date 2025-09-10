{{ config(materialized='table') }}

select
    year,
    max(case when rate_name = 'federal_funds_rate' then value end) as fed_funds_rate,
    max(case when rate_name = 'prime_rate' then value end) as prime_rate,
    max(case when rate_name = 'mortgage_rate_15yr' then value end) as mortgage_15_year,
    max(case when rate_name = 'mortgage_rate_30yr' then value end) as mortgage_30_year
from {{ ref('stg_fred_rates') }}
group by year
order by year