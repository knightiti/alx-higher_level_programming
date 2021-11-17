-- A script to Display the average temperature (Fahrenheit) by city
-- ordered by temperature (descending).

SELECT city, AVG(value) as avg_temp
FROM Temperatures
GROUP BY city
ORDER BY avg_temp DESC;
