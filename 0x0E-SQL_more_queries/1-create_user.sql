-- A script that creates a user user_0d_1 on MYSQL server

CREATE USER IF NOT EXISTS 'user_0d_1@localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1@localhost';
