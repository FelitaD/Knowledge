---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-12
sr-interval: 4
sr-ease: 230
---
|                | Integrity Constraints                                                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Classification | Integrity constraints supported in DBMS (simplest to most complicated)<br>- [[Not null]]<br>- [[Key]] (unique values)<br>- [[Referential Integrity]] (foreign key)<br>- [[Attribute-based]] (value of attribute)<br>- [[Tuple-based]] (how tuple's values relate)<br>- [[General assertions]] (use SQL queries across database) |
| Declaration    | - With original schema<br> Constraints are checked after bulk loading<br>- Later<br>Constraints will be checked on current state of db                                                                                                                                                                            |
| Enforcement    | - Check after every modification when it's susceptible to violate a constraint<br>- After every transaction (deferred constraint checking)                                                                                                                                                                        |

> There are some limits on the attribute and tuple based constraints in systems as compared to the SQL standard
> General assertions have not been implemented yet in any database system.


![[StanfordOnlineSOE.YDB-ADVSQL0001-V000200_DTH 1.mp4]]