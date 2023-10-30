-- 4. Subquery

-- Lấy customer-id và total_amount trong đó total_amount lớn hơn AVG của tất cả KH
SELECT customer_id, total_amount
FROM txn
WHERE total_amount > (SELECT AVG(total_amount) FROM txn)

-- Lấy thông tin txn của tất cả KH mà membership_level là Standard
SELECT t1.customer_id, membership_level, t1.*
FROM txn t1
JOIN (
    SELECT customer_id, membership_level
    FROM member
	WHERE membership_level = 'Standard'
) t2
ON t1.customer_id = t2.customer_id
