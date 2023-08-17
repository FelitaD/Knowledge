---
tags: tech/distributed_computing
aliases: [Concurrent, programmation concurrente]
publish: true
sr-due: 2022-11-18
sr-interval: 31
sr-ease: 240
---

Multiple computations happening at the same time (**threads, processus ou tâches**).

# Problem with concurrency in databases

Need the ability for client to execute statements against a database and not have to worry about what other clients are doing at that same time (run in isolation).

We could simply run each statement in isolation but we want to also use concurrency possibilities (when client don’t update the same portions) allowed by [[Multithreading vs. multiprocessing]], [[asynchronous IO]].

**Difficulties with concurrent access**

-   Ex. 1: attribute-level inconsistency

2 update SQL commands want to modify same attribute (eg. Stanford enrollments), might end up with 3 different values since the operation is `get` the original value, `modify` it, `put` it back

-   Ex. 2: tuple-level inconsistency

2 update SQL commands want to modify same row (student) but different fields (major and decision). The `get`, `modify`, `put` occurs in reality at the tuple level. Same problem, might end up with 2 new fields or only one.

-   Ex. 3: table-level inconsistency

1 operation’s result (accepted to Stanford) depends on if the other operation has already be made in another table (increase GPA)

-   Ex. 4: multi-statement inconsistency

We don’t want one statement to occur concurrently with the statements of another client.
