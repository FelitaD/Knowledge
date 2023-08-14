
---
tags: tech
aliases:
publish: true
sr-due: 2022-10-08
sr-interval: 3
sr-ease: 250
---

Le principe d'[[isolation]] consiste à isoler les processus.
Elle n'est pas totale car il y a besoin de communiquer avec d'autres applications (isolation contrôlée).

Le principe de [[virtualisation]] est la technique d'isolation la plus utilisée. 
Il consiste à mettre en place un environnement qui masque les outils et ressources de la machine hôte (accès à la mémoire, au CPU, au disque... en réalité traîté par des intermédiaires).

3 dispositifs de virtualisation :
- [[VM]]
	- Machine complète avec OS embarqué et ressources
	- OS consomme beaucoup de ressources
	- Système d'image (machine préparamétrée comme AMIs AWS)
- [[Containers]]
	- Pas d'OS embarqué
	- Système d'image (Docker image)
- [[Environnements virtuels]]
	- Propre à Python
	- Interpréteur et répertoire de librairies
	- Système d'image (requirements.txt)

Virtual machines vs. Docker containers
![[Pasted image 20220622000401.png]]
