select ice.flavor as "FLAVOR"
from
    (SELECT j.flavor, sum(j.total_order) as "total_order"
    FROM JULY j
    group by j.flavor
    union all
    select h.flavor, sum(h.total_order) as "total_order"
    from first_half h
    group by h.flavor) ice
group by ice.flavor
order by sum(ice.total_order) desc
limit 3