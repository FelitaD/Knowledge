---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-21
sr-interval: 11
sr-ease: 246
---

Process that ensures atomicity : undo a partial transaction to guarantee “all or nothing”

Mechanism can be used client-side : `commit else rollback`

Never hold open a transaction then wait for an arbitrary amount of time because transaction uses locking system that blocks other portions of the database (to other clients) → transactions should be constructed in a fashion that we know they are going to finish quickly.