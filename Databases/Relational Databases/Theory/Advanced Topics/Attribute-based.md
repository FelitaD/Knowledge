---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-10
sr-interval: 2
sr-ease: 250
---

`create table ( ... sizeHS int check(sizeHS < 5000))`

### Attribute constraints : enforce data consistency

#### Better data quality with constraints
`CAST AS`
```sql
SELECT CAST(some_column AS integer)

SELECT transaction_date, amount + CAST(fee AS integer) net_amount
FROM transactions;
```

#### Working with data types

`text` character strings of any length
`varchar [ (x) ]` maximum of n characters
`char [ (x) ]` fixed length of n characters
`boolean` TRUE 1 FALSE 0 or NULL
`date` `time` `timestamp`
`numeric` arbitrary precision numbers 3.1457
`integer` whole numbers in range -2147483648 +2147483648
`bigint`

- Assigning new data types
```sql
CREATE TABLE students (
ssn integer,
name varchar(64),
dob date,
average_grade numeric(3, 2), # precision 3 scale 2 -- 5.54
tuition_pais boolean
);
```

- `ALTER COLUMN TYPE` Changing the data types
```sql
ALTER TABLE table_name
ALTER COLUMN column_name
TYPE varchar(10)
```

- Convert types `USING` a function
```sql
# Truncating by keeping the first characters
ALTER TABLE table_name
ALTER COLUMN column_name
TYPE varchar(x)
USING SUBSTRING(column_name FROM 1 FOR x);
```
