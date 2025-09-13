-- Population should always be positive
select *
from {{ ref('demographics_by_metro') }}
where total_population <= 0