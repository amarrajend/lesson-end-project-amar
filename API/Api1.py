-- Find employees born on a Friday the 13th
SELECT name, birth_date 
FROM employees 
WHERE EXTRACT(DOW FROM birth_date) = 5 
AND EXTRACT(DAY FROM birth_date) = 13;

-- Recursive CTE (Fibonacci sequence)
WITH RECURSIVE fib(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n+1, b, a+b FROM fib WHERE n < 10
)
SELECT a FROM fib;
