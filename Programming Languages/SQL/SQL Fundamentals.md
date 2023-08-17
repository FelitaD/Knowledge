---
tags:
- tech
- interview
sr-due: 2022-10-14
sr-interval: 1
sr-ease: 190
---

## Introduction to SQL

### Selecting columns

```sql
SELECT col1, col2 FROM tabl;
SELECT * FROM tabl;

# Unique values in column
SELECT DISTINCT col1 FROM tabl;  

# Count rows
SELECT COUNT(*) FROM tabl;  

# Count non-missing values
SELECT COUNT(name) FROM people;  

SELECT COUNT(DISTINCT name) FROM people; 
```

### Filtering rows

#### Operators
- = equal
- `<>` not equal
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

#### WHERE
ISO Date format
```sql
SELECT name, birthdate
FROM people
WHERE birthdate = '1974-11-11';
```

#### AND OR
```sql
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');
```

#### BETWEEN
Inclusive
```sql
SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000
AND budget > 100000000;
```

#### WHERE IN
```sql
SELECT title, language
FROM films
WHERE language IN ('English', 'Spanish', 'French');
```

#### NULL, IS NULL, missing values
```sql
SELECT name
FROM people
WHERE birthdate IS NOT NULL;
```

#### LIKE  NOT LIKE
`_` match single character 
`%` match any number of characters
```sql
SELECT name
FROM people
WHERE name LIKE '_r%'; 

SELECT name
FROM people
WHERE name NOT LIKE 'A%';
```

### Aggregate functions

#### SUM MEAN MAX MIN

```sql
SELECT MIN(duration) FROM films;
```

#### Arithmetic

Division with integers returns integer
```sql
SELECT (4 / 3);
>>> 1 
```

Aliasing gives column names in output
```sql
SELECT (4.0 / 3.0) AS result;
>>> result
>>> 1.3333333

SELECT MAX(budget) AS max_budget,
MAX(duration) AS max_duration
FROM films;

SELECT title, (duration / 60.0) AS duration_hours
FROM films;

SELECT AVG(duration) / 60.0 AS avg_duration_hours
FROM films;

SELECT 45 / 10 * 100.0;
>>> 400.0
# 45 / 10 = 4.5 = 4

SELECT 45 * 100.0 / 10;
```

### Sorting and grouping

#### ORDER BY

```sql
SELECT name, birthdate
FROM people
ORDER BY birthdate; # Ascending by default

SELECT title, duration
FROM films
ORDER BY duration DESC;

SELECT name, birthdate
FROM people
ORDER BY name, birthdate; # Sort name first then birthdate
```

#### GROUP BY

```sql
SELECT sex, count(*)
FROM employees
GROUP BY sex;
```

#### HAVING

The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.

Shows only those years in which more than 10 films were released.
```sql
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10; 
```

## Joining data in SQL

### Introduction to joins

[chapter1.pdf](Web%20Scraping/chapter1.pdf)

### Outer joins and cross joins

[chapter2 (1).pdf](chapter2_(1).pdf)

### Set theory clauses

[chapter3.pdf](chapter3.pdf)

### Subqueries

[chapter4.pdf](chapter4.pdf)

## Intermediate SQL

### SET et UPDATE

Modifie colonne 1 base sur la valeur de la colonne 2

```sql
UPDATE table1
SET colonne1 = nouvelle_valeur WHERE colonne2 = valeur;
```

### We'll take the CASE

[chapter1.pdf](chapter1%201.pdf)

```sql
CASE WHEN x = 1 THEN 'a'
	 WHEN x = 2 THEN 'b'
	 ELSE 'c' 
	 END AS new_column 	
```
```sql
SELECT id, 
	 home_goal, 
	 away_goal,
	 CASE WHEN home_goal > away_goal THEN 'Home team win'
				WHEN home_goal < away_goal THEN 'Away team win'
				ELSE 'Tie' END AS outcome
FROM match
WHERE season = '2013/2014';
```
```sql
SELECT date, hometeam_id, awayteam_id,
CASE WHEN hometeam_id = 8455 AND home_goal > away_goal
	THEN 'Chelsea home win'
CASE WHEN awayteam_id = 8455 AND away_goal > home goak
	THEN ' Chelsea away win'
ELSE 'Loss or tie' END AS outcome
FROM match
WHERE hometeam_id = 8455 OR awayteam_id = 8455;
```

### Short and simple subqueries

[chapter2.pdf](Web%20Scraping/chapter2.pdf)

### Correlated queries, Nested queries, and Common Table Expressions

[chapter3.pdf](chapter3%201.pdf)

### Window Functions

[chapter4.pdf](chapter4%201.pdf)

## Functions for Manipulating Data in PostgreSQL

## PostrgreSQL Summary Stats and Window Functions


#### Update

`INSERT INTO`: Copy data from existing table to a new one


****
SQL Fundamentals : https://app.datacamp.com/learn/skill-tracks/sql-fundamentals