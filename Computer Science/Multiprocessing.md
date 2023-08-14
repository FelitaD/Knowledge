---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-19
sr-interval: 11
sr-ease: 224
---

![[Pasted image 20221008202231.png]]


L'éxécution des processus est répartie entre les coeurs du processeur qui vont donc être exécutés séparément et simultanément.

## Implementation

La librairie multiprocessing peut se révéler être une solution car elle permet de contourner le GIL en créant des sous processus au lieu de threads ce qui permet ainsi de bénéficier de meilleures performances en exploitant les différents coeurs d'un processeur.

```python
import time
import multiprocessing
from multiprocessing import Pool
import numpy as np

# On définit la fonction calcul_lourd

def calcul_lourd(x): 
    resultat = 0
    for k in range(1, 50):
        resultat += x * np.power(x, 1 / k*np.power(k,3/2))
    return resultat

t1=time.time() # On démarre la mesure du temps

# On exécute la fonction pour différents arguments à la suite

calcul_lourd(range(1000000)) 
calcul_lourd(range(5000000))
calcul_lourd(range(4000000))
calcul_lourd(range(7000000))

t2=time.time() # On arrête la mesure du temps

print("La complétion du programme en séquentiel prend : ", t2-t1)

t1=time.time() # On démarre la mesure du temps

pool = Pool(4) # On crée les processus

# On répartit l'exécution entre les coeurs
resultat = pool.map(calcul_lourd,[range(1000000),range(5000000),range(4000000),range(7000000)]) 

t2=time.time() # On arrête la mesure du temps

print("\nLa complétion du programme en parallèle prend : ",t2-t1)
```