---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-11-05
sr-interval: 15
sr-ease: 214
---

# Why Replace Relational Databases 

-   When the (unstructured) data is too hard to fit in a schema
-   Too many random reads and writes
-   Too many updates and insert (write-heavy)
-   Foreign keys and joins not really needed

# Tradeoffs for [[ACID]]

-   NoSQL db are generally focused on speed, scalability and availability
-   Consistency and / or availability often sacrified ([[CAP theorem]])
-   Data will eventually be consistent (after replication...)
-   While RDBMS provide ACID, key-value stores like Cassandra provide **BASE** :
    -   **Basically Available Soft-state Eventual Consistency**
    -   Availability > Consistency

# Characteritics

- Often use column-oriented storage
	-   Searches with only a few columns are faster (fetch only the column)
		-   relational → fetch entire table + search all the rows for the matching query
	-   Columns on different servers
	-   Easy because indexed on the key
- Schema less or schema on demand (no need to define schema in advance)
- Querying data is harder when no SQL interface
- Most have [[CRUD]]
	-   Necessary API operations : get(key) and put(key, value)
	    -   some extended operations (eg. CQL Cassandra)

# Tradeoffs between read and write performance

-   Optimized for reads or for write → high read - low write / high write - low read
-   Hotspotting issues : when client write to the same server all the time (one server is very hot) and don’t use the full potential of distribution

# Setting goals is very important

-   What is the structure of the data (does it fit to the schema design of the database) ?
-   How the data will be queried (sequential / random / small) ?
-   How does the data come in (batch, timestamps...)
-   Random or serial reads and writes ?

# Key-value abstraction

-   Dictionnary data structure → distributed
-   [DHT](https://www.notion.so/DHT-1c234570614e45b9907307c474fd0454) (Distributed Hash Tables) from P2P systems

# Workloads needs responded to by key-value stores

-   Speed (Netflix fast)
-   Avoid **SPoF** (single point of failure → server)
-   Low TCO (total cost of operation) cost of running the db
-   Fewer system administrators
-   Incremental **scalability** → **scale out** (adding machines / COTS components of the Shelf)

# Different Types of NoSQL Databases

## What NoSQL databases have in common

Non-relational databases were developed when relational databases were not able to handle the increased scale of applications following the birth of internet.

## [[Document-oriented databases]]
## [[Column-oriented stores]]
## [[Key-Value stores]]
## [[Graph-oriented databases]]
## [[Time Series databases]]
## [[Search Engines]]

# Resources

https://www.mongodb.com/scale/types-of-nosql-databases
https://datascientest.com/en/all-about-non-relational-databases