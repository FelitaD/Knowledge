---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-11-04
sr-interval: 22
sr-ease: 246
---

Normalization is a technique to reduce data redundancy and eliminate insertion, update and deletion anomalies.

#   1 NF 
- real relations with atomic values in each cell
#   2 NF 
- be in 1 NF
- specifying something about the way relations are structured with respect to their keys 
# 3 NF 
- be in 2 NF
- have no transitive functional dependencies (slight weakening of BCNF)
# BCNF
- be in 3 NF
- if functional dependency from A to B then A has to be a key
# 4 NF
- be in BCNF
- doesn't have multi-valued dependencies
# 5 NF
# 6 NF

# 1NF 
Atomicity of attributes. One attribute cannot have mutiple values
![[Pasted image 20230118132103.png|300]]

# 2NF
Conditions :
- Table has to be in 1NF
- Primary key single-column and does not contain partial dependency
Break tables apart so 1 attribute represents all the other attribute on its line 
![[Pasted image 20230118132049.png|300]]

# 3NF
![[Pasted image 20230118132002.png|300]]

****
# Resources
https://www.edureka.co/blog/normalization-in-sql/
[images source](https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.gitta.info%2FLogicModelin%2Fen%2Fhtml%2FDataConsiten_Norm3NF.html&psig=AOvVaw2KPfP96W-T4l5XORvx9Kdi&ust=1674130708673000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNDTs4ON0fwCFQAAAAAdAAAAABAW)

