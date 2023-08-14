---
tags:
- tech
- distributed
aliases:
publish: true
sr-due: 2022-10-27
sr-interval: 17
sr-ease: 210
---

Hadoop Distributed File System is the primary data storage system used by Hadoop applications. It simulates a file system.

It uses different [[Daemon|daemons]] to implement its [[Distributed systems|distributed architecture]] :

-   **Datanode**
	-   tourne sur les noeuds esclaves du container
	-   gère les données stockées sur ces noeuds esclaves
	-   intéragit avec les autres démons pour rendre les données disponibles
-   **Namenode**
    -   tourne sur noeud maître
    -   gère les méta-données sur la localisation des partitions
    -   intéragit avec datanodes pour orchestrer la lecture / écriture des données
-   **Secondary namenode**
    -   tourne sur autres noeuds maîtres
    -   reprend le rôle du master node si il tombe

![[Pasted image 20221005192513.png]]

****
https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html
