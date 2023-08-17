---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-09
sr-interval: 3
sr-ease: 250
---

Something must always be true in the db so system must verify every modification (why it's not implemented).

![[Pasted image 20220921091734.png]]

![[Pasted image 20220921091821.png]]

Exercise 1

```SQL
Faculty(name, homeDept) 
Teaches(prof, course, dept)

CREATE ASSERTION A 

(not exists (SELECT * 
			 FROM Faculty 
			 WHERE name not in 
				 (SELECT prof 
				  FROM Teaches 
				  WHERE dept = homeDept)))
```

Which cannot cause a violation :

- update to Faculty.homeDept
- deletion from Teaches
- update to Teaches.prof
- insertion into Teaches

The assertion states that every faculty member teaches at least one course in her home department. Adding a new course cannot violate the constraint.

Exercise 2

```sql
Item(category, price)

CREATE ASSERTION A

(25 < any (SELECT SUM(price) 
		   FROM item
		   GROUP BY category ))
```

Which cannot cause a violation :

- insertion into item
- deletion from item
- update to item.category
- update to item.price
