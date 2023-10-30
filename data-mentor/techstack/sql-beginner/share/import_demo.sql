-- Create a new table
CREATE TABLE demographic (
    customer_id SERIAL PRIMARY KEY,
    full_name TEXT, 
    gender TEXT,
    date_of_birth DATE,
    address TEXT,
    city TEXT,
    country TEXT,
    phone_number TEXT,
    email TEXT,
    occupation TEXT,
    education TEXT,
    marital_status TEXT
);

-- Copy data from CSV file into the table
COPY demographic(customer_id, full_name, gender, date_of_birth, address, city, country, phone_number, email, occupation, education, marital_status)
FROM '/Users/quan/work/data-dummy/sql-beginner/prepare/sql_demo.csv' WITH CSV HEADER;