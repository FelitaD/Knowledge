---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-14
sr-interval: 4
sr-ease: 210
---

L'exécution de plusieurs threads au sein d'un même coeur.

# Relation between threads and locks

Il est important de souligner que le partage de mémoire entre threads et leur exécution en parallèle est à l'origine de certaines sécurités telles que les "_locks_" ou "_synchronizers_" qui permettent d'éviter autant faire que ce peut des erreurs. 

A titre d'exemple, si l'on incrémente un même nombre entre deux threads qui sont exécutés en parallèle alors il est possible de "_perdre_" ces incrémentations car les threads ont été exécutés simultanément. Les "_synchronisations_" entre threads ainsi que des "_verrous_" permettent en règle générale d'ôter ou au moins de limiter ces erreurs.

## Multithreading in Python

Python est un cas particulier en ce qui concerne le multithreading. En effet, il possède un verrou appelé GIL pour Global Interpreter Lock en anglais qui assure qu'un seul thread n'ait accès à l'interpréteur Python a la fois. Cela rejoint ainsi la gestion des erreurs d'accessibilité de mémoire évoquée plus haut.

> Les gains perçus suite à l'utilisation de plusieurs threads sont assez limités sur Python.

```python
from threading import Thread 

# On demarre la mesure du temps 
t1=time.time() 

# On crée une liste de threads, le nombre de threads correspond au nombre de pages renseigné 
threads = [Thread(target=wikipedia_fonction, args=(page,)) for page in pages] 

# On démarre les threads 
for thread in threads: thread.start() 

# On s'assure de la complétion des threads 
for thread in threads: thread.join() t2=time.time() 

# On arrête la mesure du temps
print ("\n Durée:", (t2 - t1)) 
```
Le temps d'exécution est fortement réduit.
L'affichage des pages n'est pas dans le même ordre que décrit au sein de la liste pages.
On ne contrôle pas l'ordre de complétion des threads
