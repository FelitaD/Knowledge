---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-15
sr-interval: 5
sr-ease: 180
---

MapReduce is a programming model and implementation for processing big data on [[Distributed systems]].

MapReduce facilitates concurrent processing by splitting petabytes of data into smaller chunks, and [[Parallel processing|processing in parallel]] on Hadoop commodity servers. In the end, it aggregates all the data from multiple servers to return a consolidated output back to the application.

The two phases Map and Reduce are executed on different machines. 
- The **Map** function 
	- takes input (key, value) pairs and outputs another intermediate (key, value) pairs
	- processed on machines where the [[partitions]] are
- The Shuffle phase 
	- regroups results from a certain (key) on a same machine
- The **Reduce** function
	- takes inputs (key, value) pairs, and produces (key,value) pairs as output
	- results are aggregated per key

# WordCount : MapReduce's `hello world`

WordCount is an algorithm based on MapReduce.

Ces différentes étapes constituent un **Job** MapReduce.
-   Nombre de Mappers et de Reducers n'a pas à être le même : on peut en général choisir ces nombres.
-   Certaines machines peuvent être amenées à traiter plusieurs partitions du jeu de données ou alors à traiter un nombre important de données lors de l'étape de Reduce.
-   Ces points sont importants à prendre en compte si on ne veut pas trop ralentir la vitesse d'exécution du programme.

![[Pasted image 20221004153424.png]]
![[Pasted image 20221004153525.png]]

