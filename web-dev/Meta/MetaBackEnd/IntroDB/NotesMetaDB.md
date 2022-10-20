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