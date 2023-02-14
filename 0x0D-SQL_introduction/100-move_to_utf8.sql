-- Script to convert database
-- Use hbtn_0c_0
USE HBTN_0c_0;
-- Change name
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
-- Change table to utf-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Change database to utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
