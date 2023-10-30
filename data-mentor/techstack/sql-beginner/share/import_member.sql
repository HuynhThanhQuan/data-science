-- Create a new table
CREATE TABLE member (
    customer_id INT PRIMARY KEY,
    membership_level TEXT,
    join_date DATE,
    expiry_date DATE,
    membership_status TEXT,
    customer_points FLOAT,
    discount_rate DECIMAL(5, 2),
    referral_code TEXT,
    last_active_time TIMESTAMP, 
    num_active_last_7days FLOAT,
    num_active_last_14days FLOAT,
    num_active_last_30days FLOAT,
    total_redeemed_points FLOAT
);

-- Copy data from CSV file into the table
COPY member(
    customer_id, membership_level, join_date, expiry_date, membership_status,
    customer_points, discount_rate, referral_code, last_active_time,
    num_active_last_7days, num_active_last_14days, num_active_last_30days,
    total_redeemed_points
)
FROM '/Users/quan/work/data-dummy/sql-beginner/prepare/sql_member.csv' WITH CSV HEADER;