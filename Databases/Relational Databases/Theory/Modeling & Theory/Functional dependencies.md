When value A always determines same value B (but not the reverse). wikipedia :
![[Pasted image 20230205204202.png|1000]]

Generally useful concept for
- data storage -> compression
- reasoning about queries -> optimisation

## Functional dependencies and keys

Functional from A to B : A -> B
A is a key.

## Types of FD

### Trivial FD
A -> B is trivial if B is a subset of A

### Non-trivial FD
A -> B is non-trivial if B is not a subset of A

### Completely non-trivial FD
A and B have no intersection at all.

## Rules for FD

### Splitting rule

### Combining rule

### Trivial-dependency rules
If A determines B then A also determines
- A union B
- A intersection B

### Transitive rule
If A -> B and B -> C then A -> C

## Closure attributes

Algorithm to find all attributes B such that A -> B
Closure written with a plus sign : A+

### Closures and keys

If we compute the closure of A and we find that A determines all attributes then A is a key.



![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@FunctionalDependencies.pdf]]