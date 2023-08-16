--  a script that converts hbtn_0c_0 database 
-- to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server

-- selecting database
USE hbtn_0c_0;
-- converting tables in database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converting Field name in first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;