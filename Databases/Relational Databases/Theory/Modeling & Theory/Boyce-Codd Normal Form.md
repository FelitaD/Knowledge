---
aliases: ['BCNF']
---

**Formal definition**
A relation R with functional dependencies is in Boyce-Codd Normal Form if every functional dependencies is such that its left-hand side is a key. (Not necessarily primary key.)

**Key definition**
An attribute that determines all other attributes, if you're thinking about functional dependencies, or if you don't have any duplicates in your relation, then a key is a value that is never duplicated across tuples.

**How to transform a relation in BCNF ?**
The idea is to use the fact that in a mega relation all FDs violate the BCNF rule.


![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@BCNF.pdf]]