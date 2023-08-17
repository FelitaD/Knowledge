---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-10
sr-interval: 2
sr-ease: 230
---

`create table ( ... primary key, ... unique)`

allowed repeated null with unique constraint but not for primary key constraints

### Key constraints : uniquely identify records

[chapter3.pdf](chapter3%202.pdf)

#### Keys and superkeys
- **Key** : identify a row uniquely
- **Superkey** : combination of attributes that identify uniquely
- **Minimal superkey** : smallest combination of attribute to identify uniqueness. Also **candidate keys**

`SELECT COUNT DISTINCT` : Finding a superkey

= if equals to number of rows

#### Primary keys
- Chosen from the candidate keys
- Must always stay unique and not null

```sql
CREATE TABLE products (
product_no integer PRIMARY KEY,
name text,
price numeric
);

# Primary key with multiple attributes
CREATE TABLE example (
a integer,
b integer,
c integer,
PRIMARY KEY (a, c)
);

# Adding on existing table
ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column_name);
```

#### Surrogate keys
- Exists just for the sake of having a primary key
- `serial` Postgres data type to add unique serial numbers automatically

```sql
# Using serial
ALTER TABLE cars
ADD COLUMN id serial PRIMARY KEY;

# Combining columns
ALTER TABLE table_name
ADD COLUMN columnb_c varchar(256);

UPDATE table_name
SET column_c = CONCAT(column_a, column_b);

ALTER TABLE table_name
ADD CONSTRAINT pk PRIMARY KEY (column_c);
```
