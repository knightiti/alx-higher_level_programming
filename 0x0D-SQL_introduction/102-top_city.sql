-- Import in hbtn_0c_0 database this table dump: Temperatures
-- A script to display the top 3 of cities temperature during
-- July and August in descending order.

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = '7' OR month = '8'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
