---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-09
sr-interval: 3
sr-ease: 269
---

A transaction that has this isolation level may perform dirty reads. It will read values in the middle of another transaction before it’s committed.

`SET Transaction Isolation Level Read Uncommitted;`