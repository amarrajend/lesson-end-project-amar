-- Create an index
CREATE INDEX idx_customer_email ON customers(email);

-- Explain query plan
EXPLAIN ANALYZE SELECT * FROM large_table WHERE category = 'Electronics';
