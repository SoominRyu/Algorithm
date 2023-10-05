SELECT left(product_code, 2) as "CATEGORY", COUNT(*) as "PRODUCTS"
from product
group by CATEGORY
ORDER BY CATEGORY