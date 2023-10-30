-- 6. String
-- CONCAT
select concat(membership_level,' ', membership_status) from member

-- CONCAT with CAST
select concat(membership_status,' ', total_redeemed_points::text) from member

-- UPPER/LOWER
select UPPER(membership_status) from member

-- Tìm hiểu thêm: TRIM, REPLACE, SUBSTRING, LENGTH, POSITION, LEFT, RIGHT

-- 7. Datetime
-- NOW
SELECT NOW() AS current_datetime

-- get date from datetime
SELECT DATE(transaction_datetime) AS txn_date
FROM txn

-- Extracts a specific component (year, month, day, hour, etc.) from a datetime value.
SELECT 
EXTRACT(YEAR FROM transaction_datetime) AS year,
EXTRACT(MONTH FROM transaction_datetime) AS month,
EXTRACT(DAY FROM transaction_datetime) AS day,
EXTRACT(HOUR FROM transaction_datetime) AS hour
FROM txn

-- Interval
SELECT 
transaction_datetime,
transaction_datetime + INTERVAL '3 minutes' AS new_time,
transaction_datetime + INTERVAL '3 days' AS new_date
FROM txn

-- Age
SELECT 
join_date, expiry_date,
AGE(expiry_date, join_date) as member_lifespan
FROM member

-- 8. Number
-- Tìm hiểu thêm: POWER, ROUND, SQRT, MAX, MIN, SUM, AVG,
