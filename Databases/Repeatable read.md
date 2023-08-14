---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-12-12
sr-interval: 52
sr-ease: 269
---

An item read multiple times cannot change value  but there might be phantom tuples.

A relation can change value if it’s read multiple times through phantom tuples.

Tuples can appear — but not disappear, between 2 reads (before and after transaction) → insertions can be made by another transaction between two entire reads of a table (new tuples don’t have a lock). With deletion, we couldn’t have a read before and after the transaction since the tuples are locked after the 1st read.

`SET Transaction Isolation Level Repeatable Read;`