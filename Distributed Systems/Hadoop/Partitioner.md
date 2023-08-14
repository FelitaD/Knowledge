---
tags: tech
sr-due: 2022-10-14
sr-interval: 4
sr-ease: 270
---

Fonction de répartition des clés sur différentes machines (choix de la machine reducer) :

**number of the reducer machine**(`key`) = **HASH_FUNCTION**(`key`) **MOD** **number of reducer machines**

Gère les pbs de clé associée à un trop grand nombre de valeurs

![[Pasted image 20221010234720.png]]