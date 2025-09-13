-- No duplicates in economy_by_metro
select year, city, count(*) as row_count
from {{ ref('economy_by_metro') }}
group by year, city
having count(*) > 1