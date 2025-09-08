with source as (
    select * from {{ source('raw', 'census') }}
),

vars as (
    select * from {{ ref('census_variables') }}
),

metros as (
    select * from {{ ref('metros') }}
),

unified as (
    select
        s.year,
        -- Unified metro area code for Los Angeles
        case
            when s.geo_id = '31100' then '31080'
            else s.geo_id
        end as metro_code,
        s.var_code,
        s.name as census_name,
        s.value
    from source s
)

select
    u.year,
    u.metro_code,
    m.metro_name,
    m.metro_name_specific,
    m.state,
    u.var_code,
    v.var_name as variable_description,
    u.value
from unified u
left join vars v on u.var_code = v.var_code
left join metros m on u.metro_code = m.metro_code
