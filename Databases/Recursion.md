The general form of a recursive `WITH` query is always a _non-recursive term_, then `UNION` (or `UNION ALL`), then a _recursive term_, where only the recursive term can contain a reference to the query's own output. Such a query is executed as follows:

![[Pasted image 20230219194301.png]]
source: https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b

R actually don’t reference itself, it just references previous result and when previous result is empty table, recursion stops. Actually it could help to think of it as an iteration rather then recursion! 

# Linear Recursion

Recursion refers to the query itself.

# Non-linear Recursion

Recursion refers to itself more than once.

Non-linear converges faster and writes more concisevely than linear recursion but isn't in the SQL Standard and not implemented by DBMS.

# Mutual Recursion

Recursion refers to another recursion.
It is not implemented in Postgres.
It is part of the SQL Standard in limited form since it doesn't allow negative subqueries accross recursively defined relations.

# Recursion with Aggregation

Disallowed in the SQL Standard and not supported in any DBMS.


![[StanfordOnlineSOE.YDB-RECURSION0001-V000100_DTH.mp4]]
![[StanfordOnlineSOE.YDB-RECURSION0001-V000400_DTH.mp4]]
![[StanfordOnlineSOE.YDB-RECURSION0001-V000200_DTH.mp4]]
![[StanfordOnlineSOE.YDB-RECURSION0001-V000300_DTH.mp4]]

