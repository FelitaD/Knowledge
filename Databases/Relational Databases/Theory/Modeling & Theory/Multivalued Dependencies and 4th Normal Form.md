
Stronger than BCNF.
4NF is about the separation of independant facts.

# Multivalued Dependencies

Like functional dependencies, multivalued dependencies are based on knowledge of the real world.

> A ->> B
> says that B and the rest are independant
> If A ->> B and A ->> C then B and C are independant
![[Pasted image 20230206113204.png]]
![[Pasted image 20230206215621.png]]

Sometimes called tuple generating dependencies because definition about having additional tuples when some tuples exist. 
Unlike functional dependencies which just talk about the relationships among existing tuples.

**Real example**
![[Pasted image 20230206181129.png]]
Relationship between department and shift is nothing and there is every combination of them.

## Types

Same types as with functional dependencies

## Rules

- FD is a MVD rule
	- If we have A -> B then we also have A ->> B
		![[Pasted image 20230206121430.png|400]]
- Intersection rule
- Transitive rule

# Fourth Normal Form

Similar to FD :
> A ->> B with A is a key

Relation is in 4NF if every multivalued dependency has a key on its left hand side.

Sometimes hard to find the multivalued dependencies which make it hard to decompose with the algorithm. Should be very intuitive tho.

Decomposition examples :
>Apply(SSN, cName, hobby)  with  SSN ->> cName
>A1(SSN, cName)
>A2(SSN, hobby)
>
> StudentInfo(sID, name, dorm, major) with sID -> name and sID ->> norm
> S1(sID,name), S2(sID,dorm), S3(sID,major)

![[4NF.pdf]]

![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@MVDs4NF.pdf]]