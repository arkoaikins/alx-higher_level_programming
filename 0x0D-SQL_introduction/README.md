# SQL - Introduction
This project is an introduction to SQL(Structured Querry Language)

## What to expect from this project
|        Table of contents           |
| -----------------------------------|
|   What i learnt in this project    |
|   Comments for my SQL file         |
|   How to install MySQL on Ubuntu   |
|   How to run my SQL database       |
|   Project tasks(task 0 - task 16) -- in .sql files  |

## What i learnt in this project
This project is basically about how to issue queries in mysql
- The main conceps gotten from this project:
   - What database is and the difference between the two kinds(Relational & Non-relational database)
   - SQL
   - How to create a database in MySQL
   - What DDL and DML stand for 
   - How to CREATE or ALTER a table
   - How to select data from a table
   - How to INSERT,UPDATE or DELETE data
   - Subqueries
   - How to use MYSQL functions
 

## Comments for my SQL files
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## How to install MySQL on Ubuntu
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
- Connecting to MYSQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## How to run my SQL database
- User "container-on-demand" to run MySQL
   - In the container,credentials are root/root
```bash
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```
