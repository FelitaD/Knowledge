---
tags: tech
sr-due: 2022-10-14
sr-interval: 4
sr-ease: 270
---

Gère les pbs de clés générées plusieurs fois

Etape d’aggregation, “reduce” dans la phase Map

→ pour chaque partition du texte à étudier, une seule valeur par token émise : on réduit nettement la taille des données transmises dans l'étape de Shuffle

![[Pasted image 20221010234512.png]]
![[Pasted image 20221010234530.png]]
