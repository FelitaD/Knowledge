---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-29
sr-interval: 11
sr-ease: 184
---

![[Pasted image 20221008202110.png]]

By formal definition, **_multithreading_** refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process. 
Whereas **_multiprocessing_** refers to the ability of a system to run multiple processors concurrently, where each processor can run one or more threads.

Ainsi, lorsque l'on fait référence au [[Multithreading]], il s'agit la plupart du temps de [[Concurrency|programmation concurrente]] qui permet donc d'exploiter les temps de latence tandis que lorsque l'on fait référence au [[Multiprocessing]] il s'agit de [[programmation parallèle]] qui permet de réaliser l'exécution de plusieurs [[Processus]] en simultané.

L'exécution parallèle de threads est possible en règle générale bien que délicate compte tenu du partage de mémoire. Sur Python il n'est néanmoins possible d'exécuter qu'un seul thread à la fois à cause du GIL.

# Concurrence et parallélisme

Tâches parallèles
-   simultanées
-   indépendantes

Tâches concurrentes
-   exécution dans le même interval de temps
-   pas simultanées (illusion qu’elles sont simultanées car délai infime)
	-   CPU utilise les temps de latence pour exécuter d’autres tâches

# Choix entre thread et processus

[[IO bound]] processes
-   plusieurs threads
-   programmation concurrente (différé)
	→ Multithreading

[[CPU bound]]
-   plusieurs processus
-   programmation parallèle (simultané)
	→ Multiprocessing
	
****
https://towardsdatascience.com/multithreading-and-multiprocessing-in-10-minutes-20d9b3c6a867
