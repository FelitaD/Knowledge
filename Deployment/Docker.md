---
tags: tech/data_engineering/tools
aliases:
publish: true
sr-due: 2022-10-15
sr-interval: 5
sr-ease: 224
---

Docker utilise le principe d'[[Isolation et virtualisation]] pour implémenter la technologie de [[containerization]].
- Utilise un ensemble d'applications, librairies et exécutables, tout en reprenant l'OS de la machine hôte
- processus et containers commencent et se terminent en même temps
- Docker utilise la technologie containerd mais il en existe d'autres
- [[Docker networking]] permet de communiquer avec l'extérieur du container
	Un container se comporte comme une machine virtuelle, possède :
	- ses propres ports
	- son réseau localhost et IP locales
	- adresse IP pour communiquer avec d'autres containers dans un même **network**
	L'adresse IP peut changer au redémarrage du container, on utilise donc le nom des containers comme nom de domaine (`http://my_container:9200`).
- [[Docker volumes]] permet de persister les données
	Monter des volumes permet de :
	- persister les données entre 2 lancements de containers et même après leur suppression
	- partager des dossiers entre 2 containers
	- échanger des fichiers avec la machine hôte

Les **images** sont comme des classes et les **containers** des instances de classe.
Les images sont construites selon un système en **arborescence** :
- Image de base
	- composant 1
		- composant 2
Permet de mutualiser les ressources lorsque 2 images sont basées sur Debian par exemple, il n'est stocké qu'une seule fois.

**Docker Hub** est un répertoire contenant plus de 5 millions d'images avec notamment de nombreuses images officielles. Contient quasiment tous les outils open source.
**Docker registry** permet comme Docker Hub de distribuer ses images mais avec plus de maintenance.

Les images peuvent être **déployées sur le cloud** grâce à des solutions [[PaaS]]. Les fournisseurs permettent de lancer des containers sans avoir à se soucier de l'architecture et paramétrage de la machine hébergeant le container.

Docker a une **architecture client-serveur**.
- client : docker-cli
- serveur : docker [[Daemon]]

# Create an image

[3 ways to create images](https://medium.com/bb-tutorials-and-thoughts/docker-three-ways-to-create-container-images-and-their-use-cases-ee651c0aceef)


# Resources
https://docs.google.com/document/d/1WPEHEVaOn_oWVA11qlfV0g0vK1hQd5W4LOymQJepyms/edit?pli=1

[Best practices for Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
[Best practices for Dockerfile 2](https://www.docker.com/blog/speed-up-your-development-flow-with-these-dockerfile-best-practices/)
[Project sample](https://github.com/aiordache/demos/tree/master/dockercon2020-demo)
[Docker compose](https://docs.docker.com/compose/)
[Project skeleton samples](https://github.com/docker/awesome-compose)
