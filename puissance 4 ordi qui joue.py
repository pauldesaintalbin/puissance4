# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:54:35 2024

@author: gabouchomon
"""

import random

def initialiser_plateau(nb_lignes, nb_colonnes):
    return [[' ' for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

def afficher_plateau(plateau):
    for ligne in plateau:
        print('|'.join(ligne))
        print('-' * (len(ligne) * 2 - 1))

def coup_valide(plateau, colonne):
    return 0 <= colonne < len(plateau[0]) and plateau[0][colonne] == ' '

def obtenir_ligne(plateau, colonne):
    for ligne in range(len(plateau) - 1, -1, -1):
        if plateau[ligne][colonne] == ' ':
            return ligne
    
def placer_piece(plateau, colonne, piece):
    plateau[obtenir_ligne(plateau, colonne)][colonne] = piece

# def est_gagnant(plateau, piece):
#     for ligne in range(len(plateau)):
#         for colonne in range(len(plateau[0]) - 3):
#             if all(plateau[ligne][colonne + i] == piece for i in range(4)):
#                 return True

#     for colonne in range(len(plateau[0])):
#         for ligne in range(len(plateau) - 3):
#             if all(plateau[ligne + i][colonne] == piece for i in range(4)):
#                 return True

#     for ligne in range(len(plateau) - 3):
#         for colonne in range(len(plateau[0]) - 3):
#             if all(plateau[ligne + i][colonne + i] == piece for i in range(4)):
#                 return True

#     for ligne in range(3, len(plateau)):
#         for colonne in range(len(plateau[0]) - 3):
#             if all(plateau[ligne - i][colonne + i] == piece for i in range(4)):
#                 return True

#     return False

def est_gagnant(plateau, piece, emplacement):
    print(emplacement)
    if emplacement[0] > 2:
        print("chuis à plus dferozuifg")
    return False

def plateau_plein(plateau):
    return all(cellule != ' ' for ligne in plateau for cellule in ligne)

def jouer():
    nb_lignes = 6
    nb_colonnes = 7
    plateau = initialiser_plateau(nb_lignes, nb_colonnes)
    piece_actuelle = 'X'

    mode_jeu = input("Choisissez le mode de jeu (1 pour jouer contre l'ordinateur, 2 pour joueur contre joueur): ")

    if mode_jeu == '1':
        jouer_contre_ordinateur(plateau, piece_actuelle, nb_colonnes)
    elif mode_jeu == '2':
        jouer_joueur_contre_joueur(plateau, piece_actuelle)
    else:
        print("Mode de jeu non valide.")

def jouer_joueur_contre_joueur(plateau, piece_actuelle):
    while True:
        afficher_plateau(plateau)
        try:
            colonne = int(input(f"Joueur {piece_actuelle}, choisissez une colonne (0-{len(plateau[0])-1}): "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if coup_valide(plateau, colonne):
            placer_piece(plateau, colonne, piece_actuelle)

            if est_gagnant(plateau, piece_actuelle,
                           [obtenir_ligne(plateau, colonne), colonne]):
                afficher_plateau(plateau)
                print(f"Joueur {piece_actuelle} a gagné !")
                break
            elif plateau_plein(plateau):
                afficher_plateau(plateau)
                print("Match nul !")
                break
            else:
                piece_actuelle = 'O' if piece_actuelle == 'X' else 'X'
        else:
            print("Colonne invalide. Veuillez choisir à nouveau.")

def jouer_contre_ordinateur(plateau, piece_actuelle, nb_colonnes):
    while True:
        afficher_plateau(plateau)

        if piece_actuelle == 'X':
            try:
                colonne = int(input(f"Joueur {piece_actuelle}, choisissez une colonne (0-{nb_colonnes-1}): "))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
            
            if coup_valide(plateau, colonne):
                placer_piece(plateau, colonne, piece_actuelle)
            else:
                print("Colonne invalide. Veuillez choisir à nouveau.")
                continue
        else:
            colonne = random.randint(0, nb_colonnes - 1)
            while not coup_valide(plateau, colonne):
                colonne = random.randint(0, nb_colonnes - 1)
            placer_piece(plateau, colonne, piece_actuelle)
            print(f"L'ordinateur a choisi la colonne {colonne}.")

        if est_gagnant(plateau, piece_actuelle,
                       [obtenir_ligne(plateau, colonne), colonne]):
            afficher_plateau(plateau)
            if piece_actuelle == 'X':
                print(f"Joueur {piece_actuelle} a gagné !")
            else:
                print("L'ordinateur a gagné !")
            break
        elif plateau_plein(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break
        else:
            piece_actuelle = 'O' if piece_actuelle == 'X' else 'X'

if __name__ == "__main__":
    jouer()
