---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-29
sr-interval: 16
sr-ease: 270
---

- Add NOT NULL constraint to new table
```sql
CREATE TABLE students (
ssn integer not null,
lastname varchar(64) not null,
home_phone integer,
office_phone integer
)
```

- Remove NOT NULL constraints after creating table
```sql
ALTER TABLE students
ALTER COLUMN home_phone
SET NOT NULL;
or 
DROP NOT NULL;
```
