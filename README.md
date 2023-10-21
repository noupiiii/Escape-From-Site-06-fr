
# Escape From Site 06_fr

Escape From Site 06_fr est un petit jeu 2D développé dans le cadre de la SAE C1.
Le jeu se déroule dans le complexe 06_fr (une sorte de prison remplie de créatures)
. Le but est d'en sortir ! Malheureusement sur votre chemin vous croiserez des entitées qui ne vous laisserons pas sortir d'ici vivant.



## Authors

- [@onoupiii](https://www.github.com/noupiiii)


## Language

Language de programmation utilisé

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Demo

lien d la vidéo de démo :
## Installation

Il faut dans un premier temps installer python sur votre machine (https://www.python.org/).
Par la suite, il vous faudra installer la bibliothèque pygame
```bash
  pip install pygame
```
Vous pourrez ensuite clonner le dépôt git dans le répertoire souhaité à l'aide de la commande suivante :
```bash
  git clone https://github.com/noupiiii/Escape-From-Site-06-fr.git
```
Si vous n'avez pas git, vous pouvez installer le programme sous forme de .zip directement.

Maintenant rendez-vous dans le répertoire principal, ouvrez-y un terminal et executez la commande :
```bash
  python3 ./Main.py
```
## Règles du jeu

#### Les joueurs
Il y a 4 joueurs dans une partie. Chaque joueur est neutre par rapport aux autres. Cependant ils peuvent s'aider mutuellement à sortir du complexe.
Un joueur peut se déplacer de 1 à 6 cases par tour.

#### Les gardes
Les gardes sont des entités qui surveillent le site. S'ils vous attrapent en dehors de votre cellule, ils vous y remettront.
Les gardes peuvent se déplacer comme les joueurs (de 1 à 6 cases) de manière aléatoire à chaque tour.

#### Les SCP (pas encore implémentés)
Les SCP sont des entités que vous devez absolument fuir. S'ils vous attrapent, vous mourrez et ne pourrez plus jouer la partie.
Ils peuvent se déplacer de 1 à 12 cases par tour.

#### Les armes
Les joueurs peuvent récupérer des armes (une par joueur à la fois), ce qui leur permettra de tuer les gardes. De ce fait, s'ils tombent sur la case d'un garde, ils ne retourneront pas dans leur cellule.

#### Les cartes
Les cartes sont votre porte de sortie. Elles vous permettront d'ouvrir les 3 zones inaccessibles afin de sortir du complexe.

#### Les Zones

*Zone 1 :*  
Vous commencez dans la zone 1. Dans cette zone se trouvent des gardes, des armes et la carte de niveau 1 servant à ouvrir la zone 2.

*Zones 2-4 :*  
Ces zones (dessinées par un sol noir) sont les zones les plus dangereuses du jeu. En effet, elles abritent les SCP mais également des gardes.
Dans la zone 2 se trouve la carte permettant d'ouvrir la zone 3.
Dans la zone 4 se trouve la sortie du complexe.

*Zone 3 :*  
La zone 3 est une zone de répit. Dans celle-ci vous trouverez seulement des gardes et la carte amenant à la zone 4.
