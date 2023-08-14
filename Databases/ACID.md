---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-28
sr-interval: 15
sr-ease: 210
---

ACID are properties that define [[Transactions]] in databases. They resolve problems with concurrency and provide resilience to system failures.

# Atomicity

All or nothing. 
If the system crashes before transaction commits, it is not executed at all, else it is executed entirely.
If an application submits a transaction to a database and gets back an error, need to be aware of that process and resubmit the transaction.

# Consistency

Correctness. 
For each client and each transaction :
- all constraints hold when transaction begin
- must guarantee all constraints hold when transaction ends

# Isolation

Based on the formal concept of serializability → operations may be interleaved but execution must be equivalent to some sequential order of all transactions.

# Durability

Effects will remain in the database if system crashes after a transaction commits.
How ? Complicated protocols based on locking.
