---
tags: tech/databases, stanford
aliases:
publish: true
sr-due: 2022-10-16
sr-interval: 6
sr-ease: 210
---


```ad-summary
Transactions : 
- are a solution to both concurrency and system failure problems in databases.
- are a sequence of operations treated as a unit.
- appear to run in isolation even if many clients are operating on a database at the same time.
```

# Why transactions

To satisfy :
- [[Concurrency|Concurrent]] database access ( multiple clients)
- [[Resilience]] to system failures

Structure of DBMS :
-   Data stored on disk
-   DBMS : controls interactions with data
-   Application / web server
-   Human(s)

# Transaction properties

- Transactions support [[ACID]] properties.
- [[Transaction rollback]] undoes a partial transaction and guarantees atomicity.
- We should write transaction so that they finish quickly or else we will block portions of the database to other clients.
- Sometimes we want to relax the strictness of [[Isolation levels]] to allow more concurrency.

# Transactions exercises

-   Isolation : Suppose client C1 issues transactions T1;T2 and client C2 concurrently issues transactions T3;T4. How many different "equivalent sequential orders" are there for these four transactions ?
    t1 t2 t3 t4
    t1 t3 t2 t4
    t1 t3 t4 t2
    t3 t4 t1 t2
    t3 t1 t4 t2
    t3 t1 t2 t4

-   Consider a relation R(A) containing {(5),(6)} and two transactions: T1: Update R set A = A+1; T2: Update R set A = 2*A. Suppose both transactions are submitted under the isolation and atomicity properties. Which of the following is NOT a possible final state of R?
    6 7
    **12 14**
    10 12
    **11 13**

# SQL syntax:
-   transaction begins automatically with 1st SQL statement
-   separated with `commit`
-   `autocommit` : transform each statement into a transaction

****
[Slides](https://courses.edx.org/asset-v1:StanfordOnline+SOE.YDB-ADVSQL0001+2T2020+type@asset+block@TransactionsProperties.pdf)
