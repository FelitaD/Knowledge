---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-22
sr-interval: 11
sr-ease: 236
---

What values might be seen in the **read** transaction.

In some cases we may want to relax the notion of isolation while still providing properties that are sufficient for applications in certain circumstances.

- Isolation level is per transaction  
- Isolation levels are in the eye of the beholder
|                  | [[Dirty reads]] | non-repeatable reads | phantoms |
| ---------------- | ----------- | -------------------- | -------- |
| [[Read uncommitted]] (weakest) | ✔           | ✔                    | ✔        |
| [[Read committed]]   | 𐄂           | ✔                    | ✔        |
| [[Repeatable read]]  | 𐄂           | 𐄂                    | ✔        |
| [[Serializable read]] (strongest - default)     | 𐄂           | 𐄂                    | 𐄂        |

| | weak isolation level | strong isolation level | 
| --- | --- | --- |
| Benefits | higher [[Concurrency]] and less overhead | [[consistency]] and understandable behavior | 
| Downsides | lower [[consistency]] | reduced [[Concurrency]] and more overhead (due to locking protocols) |

#### Read only transactions
-   Independent of isolation levels
-   ==Helps system optimize performance== : less overhead than if transaction had possibility to modify.
`SET Transaction Read Only;` #flashcards

#### Isolation levels exercises
-   Consider a table R(A) containing {(1),(2)}. Suppose transaction T1 is `update R set A = 2*A` and transaction T2 is `select avg(A) from R`. If transaction T2 executes using "read uncommitted", what are the possible values it returns?
    
    3
    
    1.5
    
    2
    
    2.5

-   Consider tables R(A) and S(B), both containing {(1),(2)}. Suppose transaction T1 is `update R set A = 2*A; update S set B = 2*B` and transaction T2 is `select avg(A) from R; select avg(B) from S`. If transaction T2 executes using "read committed", is it possible for T2 to return two different values?
    
    T2 could return avg(A) computed before T1 and avg(B) computed after T1.

-   Consider tables R(A) and S(B), both containing {(1),(2)}. Suppose transaction T1 is `update R set A = 2*A; update S set B = 2*B` and transaction T2 is `select avg(A) from R; select avg(B) from S`. If transaction T2 executes using "read committed", is it possible for T2 to return a smaller avg(B) than avg(A)?
    
    avg(A) > avg(B) would require the two statements of T2 to execute between the two statements of T1, not permitted by "read committed".

-   Consider table R(A) containing {(1),(2)}. Suppose transaction T1 is `update T set A=2*A; insert into R values (6)` and transaction T2 is `select avg(A) from R; select avg(A) from R`. If transaction T2 executes using "repeatable read", what are the possible values returned by its SECOND statement?
    
    1.5 4

#### [Slides](asset-v1_StanfordOnline+SOE.YDB-ADVSQL0001+2T2020+type@asset+block@TransactionsIsolation.pdf)

