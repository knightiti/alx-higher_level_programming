-- A script that creates the database hbtn_0d_usa with the table 'cities' on my MYSQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(state_id)
);
