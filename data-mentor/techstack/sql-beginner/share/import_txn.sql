-- Create a new table
CREATE TABLE txn (
    id SERIAL PRIMARY KEY,
    transaction_id TEXT,
    transaction_datetime TIMESTAMP,
    customer_id INT,
    product_id INT,
    product_lvl1 TEXT,
    product_lvl2 TEXT,
    product_lvl3 TEXT,
    product_lvl4 TEXT,
    brand TEXT,
    price DECIMAL(10, 2),
    description TEXT,
    rating FLOAT,
    num_sold INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    total_amount INT,
    payment_id TEXT,
    promotion_id TEXT,
    transaction_status TEXT,
    transaction_type TEXT,
    store_id INT
);

-- Copy data from CSV file into the table
COPY txn(id,
    transaction_id, transaction_datetime, customer_id, product_id,
    product_lvl1, product_lvl2, product_lvl3, product_lvl4, brand, price,
    description, rating, num_sold, quantity, unit_price, total_amount,
    payment_id, promotion_id, transaction_status, transaction_type,
    store_id
)
FROM '/Users/quan/work/data-dummy/sql-beginner/prepare/sql_txn.csv' WITH CSV HEADER;
