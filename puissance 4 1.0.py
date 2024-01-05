# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:08:58 2024

@author: gabouchomon
"""

def initialiser_plateau(nb_lignes, nb_colonnes):
    return [[' ' for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

def afficher_plateau(plateau):
    for ligne in plateau:
        print('|'.join(ligne))
        print('-' * (len(ligne) * 2 - 1))

def coup_valide(plateau, colonne):
    return 0 <= colonne < len(plateau[0]) and plateau[0][colonne] == ' '

def placer_piece(plateau, colonne, piece):
    for ligne in range(len(plateau) - 1, -1, -1):
        if plateau[ligne][colonne] == ' ':
            plateau[ligne][colonne] = piece
            break

def est_gagnant(plateau, piece):
    for ligne in range(len(plateau)):
        for colonne in range(len(plateau[0]) - 3):
            if all(plateau[ligne][colonne + i] == piece for i in range(4)):
                return True

    for colonne in range(len(plateau[0])):
        for ligne in range(len(plateau) - 3):
            if all(plateau[ligne + i][colonne] == piece for i in range(4)):
                return True

    for ligne in range(len(plateau) - 3):
        for colonne in range(len(plateau[0]) - 3):
            if all(plateau[ligne + i][colonne + i] == piece for i in range(4)):
                return True

    for ligne in range(3, len(plateau)):
        for colonne in range(len(plateau[0]) - 3):
            if all(plateau[ligne - i][colonne + i] == piece for i in range(4)):
                return True

    return False

def plateau_plein(plateau):
    return all(cellule != ' ' for ligne in plateau for cellule in ligne)

def jouer():
    nb_lignes = 6
    nb_colonnes = 7
    plateau = initialiser_plateau(nb_lignes, nb_colonnes)
    piece_actuelle = 'X'

    while True:
        afficher_plateau(plateau)
        colonne = int(input(f"Joueur {piece_actuelle}, choisissez une colonne (0-{nb_colonnes-1}): "))

        if coup_valide(plateau, colonne):
            placer_piece(plateau, colonne, piece_actuelle)
            
            if est_gagnant(plateau, piece_actuelle):
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

if __name__ == "__main__":
    jouer()
