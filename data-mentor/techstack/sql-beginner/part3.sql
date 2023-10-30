-- 3. Group by
select product_lvl1, count(distinct product_lvl4) as num_products
from txn
group by product_lvl1

select customer_id, product_lvl1, sum(total_amount) as total_amount
from txn
group by customer_id, product_lvl1
order by 1,2

select customer_id, count(distinct transaction_id) as num_txn
from txn
group by customer_id

-- đếm có bao nhiêu product_lvl2 trong mỗi product_lvl1

-- tính trung bình rating của mỗi brand

-- đếm có bao nhiêu txn với mỗi transaction_type của mỗi KH

-- tính AOV (average order value) của KH, AOV = total_amount chi tiêu cua KH / tổng số order (lấy 1 order = 1 txn)