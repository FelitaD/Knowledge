---
tags: tech/databases, stanford
aliases:
publish: true
sr-due: 2022-10-08
sr-interval: 2
sr-ease: 230![[Pasted image 20230217004145.png]]
---

|              | [[Constraints]]                                                                                                                                                                   | [[Triggers]]                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Definition   | Restrict allowable data beyond those imposed by structure and type                                                                                                                | Monitor database changes<br>Event-Condition-Action-Rules : "when event occurs, check condition; if true, do action." |
| Concept      | Static                                                                                                                                                                            | Dynamic                                                                                                              |
| Examples     | 0 < GPA < 4                                                                                                                                                                       | insert application with GPA > 3.95 → accept automatically                                                            |
| Why use them | - Data entry errors (inserts)<br>- Correctness (updates)<br>- Enforce consistency<br>- Tell system about the data for storing and query processing (eg. key constraint -> unique) | - Move logic from applications to DBMS<br>- To enforce constraints (due to expressiveness[^2] and repair logic[^1])  |

[^1]: Will not only raise an error but trigger a repair action.
	When you use constraint systems, except for referential integrity, if the constraint is violated, an error is raised.
	On the other hand if you use a trigger, it can detect the constraint violated and launch an action that fixes the constraint.

[^2]: There is a large part of constraints that can't be expressed using the constraint feature but can with triggers.
	Even though the SQL standard is very expressive in terms of [[Constraints]], especially the general assertion feature, no database system implements the entire standard. Most of the constraint checking features are somewhat limited.
	On the other hand, the trigger features are quite expressive.