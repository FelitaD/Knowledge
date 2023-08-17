---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-25
sr-interval: 12
sr-ease: 247
---

Integrity of references
Foreign key constraint

> Referential integrity from R.A to S.B implies that each value in column A of table R must appear in column B of table S.

It is directional.
-   A is the foreign key
-   B is usually required to be the primary for table S or at least unique
-   Multi-attribute foreign keys are allowed (eg. cName + state)

What can violate this constraint ?
-   Insert into R
-   Delete from S
-   Update R.A
-   Update S.B

Special actions
- Delete from S / Update S.B
	-   `Restrict` (default) -> generates error when violation
	-   `Set Null` -> replace with null
	-   `Cascade`

```sql
create table ( ... references ... 
			  on delete set null,
			... on update cascade)
```
[video](StanfordOnlineSOE.YDB-ADVSQL0001-V000600_DTH.mp4)
[pdf](asset-v1_StanfordOnline+SOE.YDB-ADVSQL0001+2T2020+type@asset+block@ReferentialIntegrity.pdf)

### Foreign keys : glue tables together

[chapter4.pdf](chapter4%202.pdf)

#### Model 1:N relationships with foreign keys
- FK points to a PK of another table
	- domain and data type must be the same
	- domain of FK = domain of PK
	- **Referential integrity** : each value of FK must exist in PK
	- FK is not an actual key because duplicates and null are allowed
- Specify FK with `column_FK REFERENCES table (table_PK)`
	- naming convention **:** a foreign key referencing another primary key with name `id` is named `x_id`, where `x` is the name of the referencing table

```sql
CREATE TABLE manufacturers (
name varchar(255) PRIMARY KEY
);

INSERT INTO manufacturers
VALUES ('Ford'), ('VW'), ('GM');

CREATE TABLE cars (
model varchar(255) PRIMARY KEY,
manufacturer_name varchar(255) REFERENCES manufacturers (name)
);

INSERT INTO cars
VALUES ('Ranger', 'Ford'), ('Beetle', 'VW');
```
Throws errors since manufacturer_name doesn't exist in PK
```sql
INSERT INTO cars
VALUES ('Tundra', 'Toyota');
```
Add to existing table
```sql
ALTER TABLE a
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCES b (id);
```

- `JOIN` tables linked by a FK

#### Model N:M relationships

Eg. 4 tables

*Is affiliated with*  table represents N:M relationship and has 2 FK connecting to the two entities professors and organizations. Also adds the *function*  attribute

![Untitled](Attachments/SQL%20c675145f5bac46e8aa5eae3286dde4fe/Untitled.png)

- `SET` : copy column data from one table to another

```sql
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;
```

#### Referential integrity

*A record referencing another table must refer to an existing record in that table.*
Foreign keys prevent violations (deleting record / adding unexisting record)
Tell the database how to deal with violation `ON DELETE`:
- `NO ACTION`
Automatically added with FK. Throws an error
- `CASCADE`
Allow deletion but will also delete the referenced records
- `RESTRICT`
- `SET NULL`
- `SET DEFAULT`

Change behavior of FK from ON DELETE to CASCADE
Need to know the constraint name to delete it
```sql
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

ALTER TABLE affiliations
DROP CONSTRAINT affiliations_organization_id_fkey;

ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;
```
