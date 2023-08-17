
# Design anomalies

- Redundancy
- Update anomalies
Redundancy of CIS. If we want to update it, it must be updated 2 times.
![[Pasted image 20230201143240.png|350]]
- Deletion anomalies
- Insertion anomalies
Can't insert a tuple if we don't know yet one of the attributes (eg. student's chosen course).

# Design by decomposition

- Start with "mega" relations containing everything
- Decompose into smaller, better relations with same information
- Can do decomposition automatically :

**Automatic decomposition**
- Mega relations + properties of the data
- System decomposes based on properties
- Final set of relations satisfies normal form

# Properties and normal forms

- Functional dependencies -> Boyce-Codd Normal Form
- Multi-valued dependencies -> Fourth Normal Form

# Functional dependencies

### Transitive functional dependencies
When changing a non-key column, might cause any of the other non-key columns to change
![[Pasted image 20230131161203.png]]

### Functional dependency

SSN -> name
SSN 123 indicates Ann but the name Ann doesnt indicate always the ssn 123.

## Multi-valued dependencies

When 2 attributes are independent of each other but depend on a 3rd attribute.

![[Pasted image 20230131173143.png]]
![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@RelDesignOverview.pdf]]
