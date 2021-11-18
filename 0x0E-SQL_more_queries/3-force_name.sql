-- A script that creates the table force_name on your MySQL server.
-- use the NOT NULL constraint for the name column.

CREATE TABLE IF NOT EXISTS force_name (Id INT, name VARCHAR(256) NOT NULL);
