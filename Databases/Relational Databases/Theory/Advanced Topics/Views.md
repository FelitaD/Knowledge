# Defining and using Views
Three-level vision of database : Physical - Conceptual - Logical
- Physical : stored on disk
- Conceptual : the relations
- Logical : the views as queries on the relations
SQL syntax : `CREATE VIEW Vname(A1, A2, ..., An) AS <Query>`

![[StanfordOnlineSOE.YDB-ADVSQL0001-V001000_DTH.mp4]]
# View Modifications
Why use views :
- Hide some data from users
- Make some queries easier / more natural
- Modularity of database access
Querying views :
- Once V defined, can reference V like any table
- Queries involving V rewrittent to use base tables
Modifying views :
- Once V defined, can we modify V like any table ?
- Doesn't make sense because V is not stored on disk
- Has to make sense : views are some users' entire view of the database
Modifications to View rewritten to modify base tables :
- 1st solution : Rewriting process specified explicitly by view creator
- 2nd solution : Restrict views and modifications so that translation to base table is meaningful and unambiguous

![[StanfordOnlineSOE.YDB-ADVSQL0001-V001100_DTH.mp4]]
![[StanfordOnlineSOE.YDB-ADVSQL0001-V001200_DTH.mp4]]

## View Modifications using Triggers
1st solution to modifying views with rewritting process explicitly specified by the creator of the view.
```sql
CREATE TRIGGER CSacceptDelete
INSTEAD OF UPDATE ON CSaccept
for each row
BEGIN
	update Apply
	set cName = New.cName
	where sID = Old.sID
	and cName = Old.cName
	and major = 'EE' and decision = 'M'
END
...
```
![[StanfordOnlineSOE.YDB-ADVSQL0001-V001300_DTH.mp4]]

## Automatic View Modifications
2nd solution
System will automatically modify view if it is updatable.
Updatable Views from SQL Standard :
1. SELECT (no DISTINCT) on a single table T
2. Attributes not in view can be Null or have a default value
3. Subqueries must not refer to T
4. No GROUP BY or aggregation
`WITH CHECK OPTION` is to not add to a view a tuple that doesn't appear in the view. Guarantees that modification affects the view.

![[StanfordOnlineSOE.YDB-ADVSQL0001-V001400_DTH.mp4]]

# Materialized Views
Opposed to virtual views where Virtual View is a query that is rewritten each time you call the view. Materialized View is pre-computed so it is stored as a table. 
Pros :
- if the view is used very often then we don't need to update it each time.
Cons :
- if the view is very large, then it takes a lot of storage space
- modifications to base data that invalidate the view
Correspondance with concept of general assertions 

![[StanfordOnlineSOE.YDB-ADVSQL0001-V001500_DTH.mp4]]

## Modifications of Materialized Views
Good news : 
- just updates the stored table / view
Bad news :
- base tables still need to be modified as well
- same issues as virtual views

## Picking Materialized Views for Increased Performance
Efficiency / benefits of a materialized view depend on :
- Size of data
- Complexity of view
- Number of queries using the view
- Number of modifications affecting the view
	- also 'incremental maintenance' where we can modify the base data and propagate it to the view without doing a full recomputation (very expensive)
Similar to query / update tradeoff, materiralized views generalizes the concept of indexes.

## Automatic Query rewriting to use Materialized Views
Can increase performance significatively. For eg user wants a complex query and it is already partially computed in a materialized view.
![[StanfordOnlineSOE.YDB-ADVSQL0001-V001600_DTH.mp4]]

![[StanfordOnlineSOE.YDB-ADVSQL0001-V001700_DTH.mp4]]


