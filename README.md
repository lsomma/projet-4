# Projet
Le but de ce projet est de réaliser le jeu 2048 en python sur un TP de 3 jours.
Ce projet se déroule à deux personnes et necessite donc une répartition des tâches.

## Fonctionnalités prévues
- [x] Le jeu est fonctionnel en console
- [x] Le jeu est fonctionnel en interface graphique
- [x] Le jeu peut être relancé rapidement après une défaite ou une victoire
- [ ] Le jeu dispose d'un chronomètre
- [ ] On peut affronter un joueur en ligne
-  [ ] On peut coopérer avec un joueur en ligne (chacun joue un coup sur deux)

## Répartition des tâches
### Communs
- Etablissement d'une structure de base de l'application

### Léa
- Création des différentes tuiles
- Affichage des tuiles selon une grille de chiffre basée sur la structure décidée communement
- Gestion des événements provoqués par le joueur
- Redémarrer une partie
- Ajout du chronomètre

### Louis
- Création de la structure de la grille
- Déplacement vers le haut
- Rotation de la grille
- Ajout de tuiles aléatoires
- Test de victoire
- Test de défaite
- Gestion du mode compétitif
- Gestion du mode coopératif

## Structure de l'application
    Serveur 
    Joueur 
    Jeu
    Grille
    