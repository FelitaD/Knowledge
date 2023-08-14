
## Scaling up vs. scaling out

[[Scaling up]] / vertical scaling : augmenter la puissance d’une seule machine. 
[[Scaling out]] / horizontal scaling : ajouter des machines pour qu’elles travaillent ensemble. 

![[Pasted image 20221004141051.png]]

## Cluster of machines

### Master and worker nodes

Ensemble de [[nodes]] (machines) liés selon un schéma de communication :
-   [[master node]] : machine plus puissante, chef d’orchestre du cluster.
-   [[worker node]] / slave : exécution des tâches.

### Orchestration

 L'orchestration d'un cluster est très importante : il doit être bien orchestré pour éviter que le travail soit fait plusieurs fois, ou qu'il soit oublié. 
 Il doit exister des processus qui choisissent quelles machines font quelles actions et qui gardent une trace des machines en vie ainsi que des machines qui hébergent des données.

## Advantages of a distributed system

### More reliable and fault tolerant

Distributed systems reduce the risks of having a single point of failure.

### Increased performance

Modern distributed systems are generally designed to be scalable almost instantly.

### Partitions and replicas

[[Partition]] : données découpées en blocs (de façon homogène et dans l’ordre ou selon des critères spécifiques)
[[Réplication]] : copies des données sur les différentes machines (nombre défini par l’administrateur système)
