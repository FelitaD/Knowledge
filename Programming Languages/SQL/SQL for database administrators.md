---
tags: tech/databases
sr-due: 2022-10-09
sr-interval: 1
sr-ease: 210
---
## Introduction to Relational Databases in SQL

### Introduction

[chapter1.pdf](chapter1%202.pdf)

#### Data quality with integrity constraints

- **Attribute constraints**. Most simple constraint. Eg. data types of attributes
- **Key constraints**. Eg. primary keys
- **Referential integrity**. Glue different tables together. Eg. foreign keys

Schema = collection de tables

```sql
# Select all tables from information_schema (the metadatabase)
# with a public schemas

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

# Select all columns and their data type

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';

```

#### Tables

**Entity-relationship diagram**. Eg. 1 entity multiple attributes

`CREATE TABLE` : at least name and column with data type
```sql
CREATE TABLE weather (
clouds text,
temperature numeric,
weather_station char(5)
);
```

`ADD COLUMN` to existing table
```sql
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```
```sql
INSERT INTO organizations # target table
SELECT DISTINCT organization, organization_sector
FROM university_professors; # source table
```

`INSERT INTO`: Insert data into columns
```sql
INSERT INTO table_name (column_a, column_b)
VALUES ("value_a", "value_b");
```

`RENAME COLUMN TO`
```sql
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

`DROP COLUMN`
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

![[Attribute-based#Attribute constraints enforce data consistency]]

#### The not-null and unique constraints

![[Not null]]

- `unique`
```sql
# Add to new table
CREATE TABLE table_name (
column_name UNIQUE
);

# Add to existing table
ALTER TABLE table_name
ADD CONSTRAINT constraint_name UNIQUE(column_name);
```

![[Key#Key constraints uniquely identify records]]

![[Referential Integrity#Foreign keys glue tables together]]

####  Roundup

**Database system** = **DBMS** (Postgres) + **Database**(s)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%201.png)

[https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=13](https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=13)

## Database Design
### Intro
In database design, you have to strike a balance between modeling overhead, desired data consistency, and usability for queries.

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%202.png)

### Processing, Storing and Organizing Data

[chapter1.pdf](chapter1%203.pdf)

#### OLTP and OLAP

OLAP tools enable users to analyze multidimensional data interactively from multiple perspectives.

[Databases](https://en.wikipedia.org/wiki/Database) configured for OLAP use a multidimensional data model, allowing for complex analytical and [ad hoc](https://en.wikipedia.org/wiki/Ad_hoc) queries with a rapid execution time

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%203.png)

| OLTP tasks | OLAP tasks |
| --- | --- |
| find the price of a book | calculate books with best profit margin |
| update latest customer transaction | find most loyal customers |
| keep track of employee hours | decide employee of the month |

|  | OLTP | OLAP |
| --- | --- | --- |
| Purpose | support daily transactions | report and analyse data |
| Design | application-oriented | subject-oriented |
| Data | up-to-date, operational | consolidated, historical |
| Size | snapshot, gigabytes | archive, terabytes |
| Queries | simple transactions & frequent updates | complex, aggregate queries & limited updates |
| Users | thousands | hundreds |

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%204.png)

#### Storing data

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%205.png)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%206.png)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%207.png)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%208.png)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%209.png)

ETL example :

- eCommerce API outputs real time data of transactions
- Python script drops null rows and clean data into pre-determined columns
- Resulting dataframe is written into an AWS Redshift Warehouse

Analysts will appreciate working in a data warehouse more because of its organization of structured data that make analysis easier

#### Database design

Logic of how data is stored (how is it read / updated )

- Has a **database model**
- relational (most popular)
- NoSQL, object-oriented, network
- Has a **schema**
- must be respected when inserting data
- tables, fields, relationships, indexes and views
- [Data modeling](https://www.ibm.com/topics/data-modeling)

Visual representation of an information system

abstract → concrete :

- **Conceptual data model**

*Data structure diagrams, entity-relational diagrams, UML*

- Designed at the beginning of a project
- Typically include entity classes, their characteristics and relationships between them
- Simple notation
- **Logical data model**

*Data warehouses, database models and schemas, relational model, star schema*

- Provide greater detail about concepts and relationships
- Indicate data attributes (data types and length), relationships
- Notation follows a formal system
- **Physical data model**

*Partitions, CPUs, indexes, backup systems, tablespaces*

- Schema for how data will be physically stored
- Final design that can be implemented as a relational database
- Associative tables, relationships with PK and FK, DBMS specific properties (performance tuning...)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%2010.png)


![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%2011.png)

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled%2012.png)

![Untitled](Untitled%2013.png)

Dimensional table hold the primary keys and will have foreign keys in the fact table


### Database Schemas and Normalization

### Database Views

### Database Management


## Creating PostgreSQL Databases
### Structure of PostgreSQL Databases

[chapter1 (1).pdf](chapter1_(1).pdf)

- Creating a database

`CREATE DATABASE db_name`

- Creating tables

`CREATE TABLE table_name ();`

- Creating schemas

Collection of tables that provide separate environments for different users & a way to organise the database

`public`  default in Postgres

`CREATE SCHEMA schema_name;`

`CREATE TABLE schema_name.table_name ()`

### PostgreSQL Data Types

[chapter2 (1).pdf](chapter2_(1)%201.pdf)

### Database Normalization

### Access Control in PostgreSQL

[chapter4.pdf](chapter4%203.pdf)

#### Introduction
- Default superuser
`postgres` administers db with privileges :
	- creating db
	- dropping db
	- inserting records
	- deleting records
- User with restricted access :
	- adding records
	- querying records
	- editing records
	- Use `postgres` when need to change db structure (add column...)
	`CREATE USER newuser WITH PASSWORD 'secret';`
	→ can create tables in database but not access tables created by other users
	`ALTER USER newuser WITH PASSWORD 'new_secret';`

#### PostgreSQL access privileges

Types of roles :
- Users
- Groups

User who creates db owns it. other can access it if `GRANT`ed + `SELECT` / `DELETE` / `UPDATE`

Give privilege `p` on db object `obj` :
`GRANT p ON obj TO grantee;`

Eg. `GRANT DELETE ON loan TO sgold;`

Some privileges cannot be granted : `ADD COLUMN`, `RENAME COLUMN`
Instead, give ownership of the table :
`ALTER TABLE table OWNER TO new_owner`;

#### Hierarchical access control

Eg. Share finance database with a spouse
```sql
CREATE SCHEMA me;
CREATE SCHEMA spouse;

CREATE TABLE me.account (...);
CREATE TABLE spouse.account (...);

CREATE USER robert WITH PASSWORD 'changeme';
GRANT USAGE ON SCHEMA spouse TO robert;
GRANT USAGE ON SCHEMA public TO robert;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA spouse
TO robert;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public
TO robert;
# Not me schema
```

Then you have children
Grant privilege on a group then add user that will automatically have the privileges of the group.
```sql
CREATE GROUP family;
GRANT USAGE ON SCHEMA public TO family;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public
TO family;
ALTER GROUP family ADD USER fiona;
ALTER GROUP family ADD USER robert;
```

#### Removing access

## Improving Query Performance in PostgreSQL

****
SQL for Database Administrators : https://app.datacamp.com/learn/skill-tracks/sql-for-database-administrators?version=1