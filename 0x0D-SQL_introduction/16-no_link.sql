-- A script to lists all records of second_table in the database hbtn_0c_0
-- Exclude rows without a name value
-- Results should display the score, then the name.
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command

SELECT `score`, `name`
FROM second_table
WHERE name IS NOT NULL
ORDER BY `score` DESC;
