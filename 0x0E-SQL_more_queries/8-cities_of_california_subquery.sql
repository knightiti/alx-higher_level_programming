-- A script that lists all the cities of California found in database 'hbtn_0d_usa'
SELECT id, name
FROM cities
WHERE state_id =
	(
		SELECT id
		FROM states
	         WHERE id = '1'
	);
