-- Income to Price Ratio should not be negative
select *
from {{ ref('housing_vs_income') }}
where income_to_price_ratio < 0