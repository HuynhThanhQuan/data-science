-- 9. Thực hành tạo feature
-- Đếm số lượng transaction trên mỗi user trong 3,6,9,12,24 tháng gần nhất
SELECT 
    customer_id,
    COUNT(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '3 months' THEN 1 END) AS transaction_count_3_months,
	COUNT(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '6 months' THEN 1 END) AS transaction_count_6_months,
	COUNT(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '9 months' THEN 1 END) AS transaction_count_9_months,
	COUNT(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '12 months' THEN 1 END) AS transaction_count_12_months,
	COUNT(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '24 months' THEN 1 END) AS transaction_count_24_months
FROM 
    txn
GROUP BY 
    customer_id

-- Tổng tiền transaction trên mỗi user trong 3,6,9,12,24 tháng gần nhất
SELECT 
    customer_id,
    SUM(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '3 months' THEN total_amount ELSE 0 END) AS total_amount_3_months,
	SUM(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '6 months' THEN total_amount ELSE 0 END) AS total_amount_6_months,
	SUM(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '9 months' THEN total_amount ELSE 0 END) AS total_amount_9_months,
	SUM(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '12 months' THEN total_amount ELSE 0 END) AS total_amount_12_months,
	SUM(CASE WHEN transaction_datetime >= DATE('2023-01-01') - INTERVAL '24 months' THEN total_amount ELSE 0 END) AS total_amount_24_months
FROM 
    txn
GROUP BY 
    customer_id

-- Đếm số lượng transaction mà khách hàng hủy
SELECT 
    customer_id,
	COUNT(CASE WHEN transaction_status = 'Đã hủy' AND transaction_datetime >= DATE('2023-01-01') - INTERVAL '3 months' THEN 1 END) AS canceled_count_3_months,
    COUNT(CASE WHEN transaction_status = 'Đã hủy' AND transaction_datetime >= DATE('2023-01-01') - INTERVAL '6 months' THEN 1 END) AS canceled_count_6_months,
    COUNT(CASE WHEN transaction_status = 'Đã hủy' AND transaction_datetime >= DATE('2023-01-01') - INTERVAL '9 months' THEN 1 END) AS canceled_count_9_months,
    COUNT(CASE WHEN transaction_status = 'Đã hủy' AND transaction_datetime >= DATE('2023-01-01') - INTERVAL '12 months' THEN 1 END) AS canceled_count_12_months,
    COUNT(CASE WHEN transaction_status = 'Đã hủy' AND transaction_datetime >= DATE('2023-01-01') - INTERVAL '24 months' THEN 1 END) AS canceled_count_24_months
FROM 
    txn
GROUP BY 
    customer_id

