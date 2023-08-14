---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-17
sr-interval: 9
sr-ease: 230
---

Sous partie [[Processus]] / fil d’exécution d’instructions.
-   parallèles ou concurrents
-   **partagent un espace mémoire** (threads d’un même processus) → communication moins coûteuse entre threads

In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), a **thread** of [execution](https://en.wikipedia.org/wiki/Execution_(computing) "Execution (computing)") is the smallest sequence of programmed instructions that can be managed independently by a [scheduler](https://en.wikipedia.org/wiki/Scheduling_(computing) "Scheduling (computing)"), which is typically a part of the [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system").

The implementation of threads and [processes](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)") differs between operating systems, but in most cases a thread is a component of a process. 

The multiple threads of a given process may be executed [concurrently](https://en.wikipedia.org/wiki/Concurrent_computation "Concurrent computation") (via multithreading capabilities), sharing resources such as [memory](https://en.wikipedia.org/wiki/Shared_memory_(interprocess_communication) "Shared memory (interprocess communication)"), while different processes do not share these resources. In particular, the threads of a process share its executable code and the values of its [dynamically allocated](https://en.wikipedia.org/wiki/Memory_management#HEAP "Memory management") variables and non-[thread-local](https://en.wikipedia.org/wiki/Thread-local_storage "Thread-local storage") [global variables](https://en.wikipedia.org/wiki/Global_variable "Global variable") at any given time.

![[Pasted image 20221005181118.png]]
[Program](https://en.wikipedia.org/wiki/Computer_program "Computer program") vs. [Process](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)") vs. Thread [Scheduling](https://en.wikipedia.org/wiki/Scheduling_(computing) "Scheduling (computing)"), [Preemption](https://en.wikipedia.org/wiki/Preemption_(computing) "Preemption (computing)"), [Context Switching](https://en.wikipedia.org/wiki/Context_switch "Context switch")
