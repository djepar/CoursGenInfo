Introduction to Databases for Back-End Development
Meta
# Databases and data 
## Type of data contains in database
- Object-oriented database --> data store as objects
- Graph databases --> data stored as nodes
- document databases --> stored as JSON objects

## How is data related?
The columns is call the fields
The rows are call rows. 
A whole row is an entity
"A Primary Key field contains unique values that cannot be replicated elsewhere in the table. This avoids potential confusion between tables with similarities in data"
"A foreign key is a field in one table that connects to the primary key field in the original table"

## Alternative types of databases
- Relational databases: "Used or storing structured data in tabular format".
- NoSQL databases : "provide a flexible structure for storing and scaling data"
  - "Document databases
  - Key-value databases
  - Graph databases"

Big data is 
- Types of data "combination of structured, semi-structured and unstructured data"
- Data power: "more powerful than traditional data when solving problems"
- Data insights : "Provides unique insights to help improve decision making"

## Database Evolution
"""
- (1970s-1990s) - Flat files, hierarchical and network
- (1980s-present) - Relational
- (1990s-present) - Object-oriented, object-relational, web-enabled
"""

## Additional reading
### The ACID properties of the relational databases:
"""
- Atomicity : All changes to data are performed as if they are a single operation. That is, all the changes are performed, or none of them are. 
- Consistency : Data remains in a consistent state from state to finish, reinforcing data integrity
- Isolation : The intermediate state of a transaction is not visible to other transactions, and as a result, transactions that run concurrently appear to be serialized. 
- Durablity : after the successful completion of a transaction, changes to data persist and are not undone, even in the event of a system failure.

"""
from : https://www.ibm.com/cloud/learn/relational-databases

Difference between relational database vs relational database management system 
The relational database is the content while the management system is the software that control it like MySQL (https://www.ibm.com/cloud/learn/relational-databases)

# Intro to SQL
SQL : "Standard language that can interact with structured data on databases."

"A database interprets and make sense of SQL instructions with the use of a Database Management System (DBMS)

## SQL usage
CRUD operations :
- Create
- Read
- Update
- Delete

SQL subsets :
- Data Definition Language (DDL)
  - DDL Create commande : "Used to create storage objects in a database, like a tables"
  - DDL Drop command : "Remove an existing object form a database".
- Data Manipulation Language (DML)
  - DML Insert command : "Insert records of data into a database table"
  - DML Delete command : "Delete one or more rows of data from a table"
- Data Query Language (DQL)
  - DLQ Select command : "retrieve data from one or multiple tables letting you specify the data fields that you want based on preferred filter criteria"
- Data Control Language (DCL)
  - DLC commands : "Grant and revoke DCL commands are used to give users access privileges to data, and to revert access privileges already given to users".

## Advantages of SQL
- User-friendly : "SQL requires very little coding skill to use".
- Standard language : "compatible with all available relational databases".
- Portable language : "SQL can be used on any hardware running any OS."
- "covers all areas of database management administration".
- Data processing : "SQL processes large amounts of data quickly and efficiently".

## SQL syntax introduction
### Create a database and tables using the DDL subset of SQL

__CREATE__ Command 
Syntax : 
- `CREATE DATABASE College;`
- `CREATE TABLE  Student;`
Example
`CREATE DATABASE College;`
`CREATE TABLE  Student;`
__ALTER__ Command :
"To change the structure of a table sin the database such as changing the name of a table, adding a primary key to a table, or adding or deleting a column in a table.
1. Syntax to add a column into a table: `ALTER TABLE table_name ADD (column_name datatype(size))`
2. Syntax to add a primary key to a table: `ALTER TABLE table_name ADD primary key (column_name);`

__DROP__ Command :
To delete a datable or a table
`DROP TABLE table_name;`

__TRUNCATE__ Command
"Remove all records from a table, which will empty the table but not delete the table itself"
`TRUNCATE TABLE table_names;`

__COMMENT__ Command
`--This is a comment`

### Utilize the DML subset of SQL to populate and modify data in a database
__SELECT__ Command:
"To retrieve data from tables in the database."
`SELECT * FROM table_name;`




__INSERT__ command :
```
INSERT INTO table_name (column_one, column_two, column_three...) VALUES (value1, value2, value3, ...);
```
Example :
```
INSERT INTO Student (column_ID, first_name, last_name...)
VALUES(value1, value2, value3, ...)
```

__UPDATE__ Command
"Update or modify data contained within a table in the database."
Syntax : `UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;`
Example : 
```
UPDATE Student
SET data_of_birth = "2000-10-12"
WHERE ID = 02;
```

__DELETE__ Command
Delete data from a table in the database
Syntax : `DELETE FROM table_name WHERE condition;`
```
DELETE FROM Student 
WHERE ID = 03;
```

### Read and query data within databases using the DQL subset of SQL
Query data within a table:
```
SELECT first_name, last_name,
FROM Student
WHERE ID = "01"
```

### DLC Commands
- GRANT
- REVOKE

### TLC Commands
- COMMIT : "Command to save all the work you have already done in the database".
- ROLLBACK : "Command to restore a database to the last committed state"

# Basic database structure
## What are tables in databases?
### What are a database table at a conceptual level
"A table is made up of rows and columns which hold data"
"A table is stored in a database [which can] holds multiple tables."
"A table is also known as an entity"
 

### Explain how data is structured in a database table
Inside a table there is columns (also called fields)
- Data Type
  - Numeric : INT, TINYINT, BIGINT, FLOAT, REAL
  - Char and string : CHAR, VARCHAR
  - Date and Time : DATE, TIME, DATETIME
  - Binary: BINARY, VARBINARY
  - Other
    - "Character Large Object(CLOB) : for storing a large block of text in some form of text encoding.
    - Binary Large Object (BLOB) for storing a collection of binary data such as images.
- SQL interaction

## Table overview

Primary key : "In a table, [the] field or column that is knows as a key which can uniquely identify a particular tuple (row) in a relation (table)."
Can also be composite (a set of two columns make a key)

Foreign key : "Takes are linked with one another through a key column (the primary key) of one table that's also present in the related tables as foreigh key"

Integrity constraints 
- Key constraints : "The key constraint specifieds that there should be a column, or columns, in a table that can be used to fetch data for any row" (the primary key, which should never have the value NULL)
- Domain constraints : "Domain constraints refer to the rules defined for the values that can be stored for a certain column."
- Referential integrity constraints : "When a table is related to another table via a foreign key column, then the referenced column value must exist in the other table."

## Types of keys in a database table

Key attribute : "Used to uniquely identify an individual record of data"

Candidate key attribute : "Any attribute that contains a unique value in each row of the table"

Composite key attribute : "A key composed of two or more attributes to form a unique value in each new row."

Alternate key : "A candidate key not selected as the primary key"

Foreign key : "An attribute that references a unique key in another table"


# SQL data types 
Data types : "Datatypes tell a database management system how to interpret the value of a column"

## Numeric data types
Numeric data types : "The datatypes that let columns store data as numbers within the database".
- TINYINT 0-255 (+ or -)
- INT 4BILLIONS (+ or -)

## String data types
- char : "the given length of characters is predetermined" ex : var(50)
- varchar : "the given length of characters is variable" varchar(50)
- TinyText : < 255 char
- text < 16.7 millions
- medium > 16.7 millions < 4gig of data
- longtext < 4gig

## Default values
Database constraints : "Limit the type of data that cna be stored in a table"
- NOT NULL : "The NOT NULL SQL contraints is used to ensure the data fields are always completed and never left blank."
  - NOT NULL SQL statement : `CREATE TABLE Customer(customer_id int NOT NULL, customer_name varchar(255) NOT NULL);`
- Default : "sets a default value for a column of no value is specified"
  - Default statement : `CREATE TABLE Customer(customer_name varchar(255) default "Bonjour");`

## Create and read
### CREATE and DROP database
- To create a database : `CREATE DATABASE database_name;`
- To drop a database : `DROP DATABASE database;`

### CREATE TABLE statement
- Create table :  `CREATE TABLE table_name( column1_name DATATYPE...);`
  - Ex : `CREATE TABLE customers(customerName VARCHAR(100), phoneNumber INT);`

### ALTER TABLE statement
- Alter table syntax : `ALTER TABLE table_name ADD (column_name DATA TYPE)`
  -  Ex 
     - `ALTER TABLE students ADD(age INT, country VARCHAR(50), nationality VARCHAR(255))`
     - `ALTER TABLE students DROP COLUMN nationality;`
     - `ALTER TABLE students MODIFY country VARCHAR(100);`

### Insert statement
- Insert syntax : `INSERT INTO table_name (column1_name, column2_name, column3_name) VALUES (value1, value2, value3);`
  - or `INSERT INTO table_name (column1_name, column2_name, column3_name) VALUES (value1, value2, valu3),(value1, value2, valu3), (value1, value2, valu3))`
Ex : 
```
INSERT INTO players(ID, name, age, start_date) VALUES (1, "Yuval", 25, "2020-10-15")
INSERT INTO players(ID, name, age, start_date) VALUES(2, "Mark", 27, "2020-10-12"), (3, "Karl", 26, "2020-10-07");
SELECT * FROM players;
```

### SELECT statement
Select syntax : `SELECT column FROM table;
Ex : 
- `SELECT playername FROM player_tbl;`
- `SELECT ID, name, age, level FROM table;`
- `SELECT * FROM table;`

### INSERT INTO SELECT statement
"The INSERT INTO select statement is used to query data from a column within a source table and place the results of that query in the column within a target table"

INSERT INTO SELECT statement syntax : 
```
INSERT INTO target_tbl(column_name) 
SELECT column_name 
FROM source_tbl;
```

Ex : `INSERT INTO country(countryName) SELECT country FROM players`

## Updating data
UPDATE statement syntax : 
```
UPDATE TABLE_NAME 
SET col_name = 'new value'
WHERE ID = 1;
```

Example one field one student: 
```
SELECT * FROM student_tbl WHERE 1
UPDATE student_tbl
SET home_address = '234 Avenue', contact_number = '223324'
WHERE ID = 3;
```

Example one field for multiple all students :
```
UPDATE student_tbl
SET college_address = 'Harper Building'
WHERE department = 'engineering';
```

Example multiple field for multiple student :
```
SELECT * FROM 'student_tbl` WHERE 1
SET college_adress = 'Harper Building', home_address = 'xyz'
WHERE department = 'engineering';
```

## Deleting data
DELETE statement syntax : 

Example one field one student : 
```
DELETE FROM student_tbl
WHERE last_name = 'Millar';

```

Example one field multiple students : 
```
DELETE FROM student_tbl
WHERE department = 'engineering';
```


# SQL operators
Operators : "Words or characters used to perform activities in a database"

General syntax : `SELECT Column_Name_1 Operator Column_Name2 FROM Table_Name;` 
(from https://www.javatpoint.com/sql-arithmetic-operators)

General syntax with condition : `SELECT Column_Name_1 Operator Column_Name2 FROM Table_Name WHERE Condition;` 
(from https://www.javatpoint.com/sql-arithmetic-operators)
## SQL Arithmetic Operators

Arithmetic operators : "used to perform mathematicla calculations in a database"
- Addition
  - Ex : `Select 5 + 5` = 10
  - `SELECT column_name1 + column_name2 FROM table_name;`
  - ` SELECT * FROM employee WHERE salary+ allowance = 25000;`
- Subtraction
  - Ex : `Select 5 - 5` = 0
  - `SELECT column_name1 - column_name2 FROM table_name;`
  - `SELECT salary-tax FROM employee;`
  - `SELECT * FROM employee WHERE salary - tax = 50000;`
- Multiplication
  - Ex : `Select 5 * 5` = 25
- Division
  - Ex : `Select 5 / 5` = 1
- Modulus
  - Ex : `Select 5 % 5` = 10

## SQL Comparaison operators
SQL Comparaison operators "are used to compare two values or expressions where the outcome result can be either true or false"

- Equal to : =
  - Ex : `SELECT * FROM employee WHERE salary = 18000;`
- Less than (or equal to) /  : <(=)
  - Ex : `SELECT * FROM employee WHERE salary < 18000;`
- Greater than (or equal to) : >(=)
- Ex : `SELECT * FROM employee WHERE salary >= 18000;`
- Inequality : <> or !=