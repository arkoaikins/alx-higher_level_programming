-- cript that creates the database hbtn_0d_2 and the user user_0d_2

-- query to create the database  hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- query to crate the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- query to give the user user_0d_2 created read privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
