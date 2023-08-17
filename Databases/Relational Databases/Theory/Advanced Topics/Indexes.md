---
tags: tech/databases, stanford
aliases:
publish: true
sr-due: 2022-10-08
sr-interval: 2
sr-ease: 224
---

```ad-summary
- Indexes are the primary way to optimize queries.
- 2 types : hash and tree-based for equality and inequality.
- Index help find portions of a table quickly.
	-   Benefits of an index depend on size of table, data distributions, workload, etc.
	-   Downsides significant when updates more frequent than queries due to index maintenance.
- Best indexes determined with the physical design advisor based on the query optimizer (one of the most important component of a database).
```


An index is a persistent [[Data Structures]] that resides with the data.

It is the primary way to *optimize queries* : right indexes can get orders of magnitude (x10, x100...) of performance improvement.


### Underlying data structures

| | [[Hash tables]] | Balanced trees (B-trees, B+ trees) | 
| --- | --- | --- | 
| condition | = | = ≤ ≥ | 
| running time | constant | logarithmic |

Many DBMS build index automatically on PRIMARY KEY / UNIQUE

### Downsides (cost > benefits)

-   Index maintenance (significant)
-   Index creation time (medium)
-   Extra-space (marginal)

> For a db that is modified often and not queried as much → cost of maintenance (updating index at each modification) offsets the benefits of having an index    

### Benefits of an index depend on

-   Size (and possibly layout) since index help finding specific portions of a table quickly
	- small tables reduce benefits 
	- big tables increase benefits
-   Data distributions
-   Query vs. update load or frequency since updating implies rebuilding the index
	- updates reduce benefits of an index
	- queries increase benefits of an index

> The performance of a big table with more frequent queries than updates will benefit a lot from an index.

### Physical design advisor

Determines which index to build on a database. Relies on the query optimizer.

-   Input
    -   database statistics : how large are the tables and their distribution
    -   workload : queries and updates expected with their frequency
-   Output
    -   recommended indexes that will speed up the overall workload

### Query optimizer

One of the most important component of a database. 
Takes a query and figure out how to execute it :

-   Input : statistics, query or update command, indexes that currently exist
-   Explore various ways of actually executing the query : which indexes will be used, which order things will be done in, estimates the cost
-   Output : estimated best execution plan with estimated cost

[Slides](https://courses.edx.org/asset-v1:StanfordOnline+SOE.YDB-ADVSQL0001+2T2020+type@asset+block@Indexes.pdf)

## Exercises

-   Which index cannot be useful in speeding up query execution ?
    
    ```sql
    SELECT * FROM Apply, College
    WHERE Apply.cName = College.cName
    	AND Apply.major = 'CS' 
    	AND College.enrollment < 5000
    ```
    
    -   Tree-based index on Apply.cName
    -   Hash-based index on Apply.major
    -   Hash-based index on College.enrollment
    -   Hash-based index on College.cName

-   Suppose we are allowed to create 2 tree-based indexes : which ones are most useful for speeding up query execution?
    
    ```sql
    SELECT * FROM Student, Apply, College
    WHERE Student.sID = Apply.sID 
    	AND Apply.cName = College.cName
    	AND Student.GPA > 1.5 
    	AND College.cName < 'Cornell'
    ```
    
    -   Apply.cName, College.cName
    -   Student.sID, Student.GPA
    -   Student.sID, College.cName
    -   Apply.sID, Student.GPA
    
#### R
An index on Student.sID can be used for its join condition and an index on College.cName can be used for both its join condition and 'cName < Cornell.'

```
    An index on Student.GPA is unlikely to be helpful since most students satisfy GPA > 1.5.
    
    Indexing both Apply.cName and College.cName helps with only one join condition.
```