---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-07
sr-interval: 1
sr-ease: 208
---

# SQL Standard for Triggers
```sql
CREATE Trigger name

Before|After|Instead Of events
# events : insert, delete, update on table

[referencing-variables]
# reference the variables that caused the trigger to be activated
# for an insert -> only new data referenced
# for a delete -> only old data referenced
	# old row -> specific row that was deleted
	# old table -> all rows that were deleted
# for an update -> both old and new data referenced

[For Each Row] 
# optional : trigger activated once for each modified tuple
# eg. on delete -> dont specify [for each row] so trigger only once if delete multiple rows
# Present = row-level 
# Not present = statement-level

WHEN (condition)
# Similar to WHERE

action
```

# Row-level vs Statement-level
2 triggers equivalent to express referential integrity constraints :
```sql
# Row-level

Create Trigger Cascade
After Delete On S
Referencing Old Row As O
For Each Row
# [ no condition ]
Delete From R Where A = O.B

# Statement-level

Create Trigger Cascade
After Delete On S
Referencing Old Table As OT
# [ For Each Row ]
# [ no condition ]
Delete From R Where A in (Select B from OT)
```
>R.A references S.B, cascaded delete ( if we delete from table S then any values A that reference the deleted B will themselves also be deleted )

Which level to chose depends on :
-   if the system supports it
-   for the example statement-level more efficient since delete in one time sufficient

# Tricky issues with triggers
-   Row-level vs. Statement-level
    -   New/old row/table
    -   Before, Instead Of
-   Multiple triggers activated at same time → which goes first
-   Trigger actions activating other triggers (chaining)
    -   also self-triggering, cycles, nested invocations (when trigger has multiple actions that individually activate other triggers)
-   Conditions in `WHEN` vs. as part of `action`
    -   see what system supports
    -   see efficiency
-   Implementations vary significantly
    -   SQLite : only row-level

[[Demo]]
![[asset-v1_StanfordOnline+SOE.YDB-ADVSQL0001+2T2020+type@asset+block@Triggers_Demo1.pdf]]
![[triggers.pdf]]
