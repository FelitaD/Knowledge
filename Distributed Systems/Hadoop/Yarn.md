---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-21
sr-interval: 11
sr-ease: 250
---

```ad-summary
Yet Another Resource Negociator
-   orchestration des Jobs
-   attribution des ressources
```

# Daemons

-   **Resource manager**
    -   tourne sur master node
    -   attribue ressources aux slave nodes qui participent au Job
-   **Application manager**
    -   déclenché par un client souhaitant faire un Job [[MapReduce]]
    -   demande les ressources au Resource manager
-   **Node manager**
    -   tourne sur tous les slave ndoes
    -   intéragit avec 2 précédents managers pour informer sur l’avancement du travail
-   **Containers**
    -   des JVM (Java Virtual Machine)
    -   effectuent le travail avec mémoire et disque alloués

# En pratique

-   Création d’une application (jobs mapreduce)
    -   informations sur localisation dans [[HDFS]]
    -   nombre de mappers
    -   nombre de reducers
    -   code du MapReduce
    -   code du [[Combiner]]
    -   code du [[Partitioner]]
-   Lancement de l’application
    -   Resource manager déclenche l’exécution d’un Application manager sur un node
    -   Application manager demande au Resource manager les mappers, reducers...
    -   Resource manager lance les JVM sur les nodes et transmet leurs adresses à l’Application manager
-   Exécution de l’application
    -   Application manager orchestre le travail
    -   Communications passent par le Resource manager ( réseau de type share-nothing)

![[Pasted image 20221004155009.png]]
![[Pasted image 20221004155028.png]]
![[Pasted image 20221004155047.png]]
![[Pasted image 20221004155103.png]]
![[Pasted image 20221004155124.png]]
