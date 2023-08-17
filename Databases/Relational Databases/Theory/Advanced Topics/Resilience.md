---
tags: tech
aliases:
publish: true
sr-due: 2022-10-19
sr-interval: 9
sr-ease: 246
---

We want all or nothing when a crash occurs, not half of the data lost in limbo.

**Resilience to system failures**

What happens if we are bulk loading or moving data and there is power going out in the middle of it ?

Databases do update by bringing data from disk to memory then back to disk → same problem if there is a crash.
