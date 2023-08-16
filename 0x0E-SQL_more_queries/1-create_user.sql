-- script that creates the MySQL server user user_0d_1

-- query to create the user  user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY "user_0d_1_pwd";
-- query to grant user_0d_1 all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
