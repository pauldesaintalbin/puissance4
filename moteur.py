import numpy, copy, random

def initialiser_plateau(nb_lignes, nb_colonnes):
    return [[' ' for i in range(nb_colonnes)] for i in range(nb_lignes)]

def coup_valide(plateau, colonne):
    return 0 <= colonne < len(plateau[0]) and plateau[0][colonne] == ' '

def obtenir_ligne(plateau, colonne):
    """ Renvoie l'indice de la ligne libre la plus basse dans la colonne
    donnée et -1 si la colonne est pleine """
    index_ligne = -1
    for ligne in range(len(plateau) - 1, -1, -1):
        if plateau[ligne][colonne] == ' ':
            index_ligne = ligne
            break
    return index_ligne
        
def stocker_piece(plateau, colonne, piece):
    plateau[obtenir_ligne(plateau, colonne)][colonne] = piece
    
def est_gagnant_minimax(plateau, piece):
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
def est_gagnant(plateau, piece, emplacement):
    # Si la pièce est a au moins 3 pièces en dessous d'elle,
    # on regarde si il y a un alignement vertical
    nb_pieces_alignees = 1
    if emplacement[0] <= 2:
        for i in range(1, 4):
            if plateau[emplacement[0] + i][emplacement[1]] == piece:
                nb_pieces_alignees += 1
            else:
                nb_pieces_alignees = 1
                break
    if nb_pieces_alignees >= 4:
        return True
    
    # On regarde s'il y a un alignement horizontal
    # On regarde d'abord le nombre de pièces de la même couleur de piece
    # qui y sont collées à GAUCHE
    for i in range(1, min(3, emplacement[1]) + 1): # Permet de ne pas sortir de la grille lors de la vérification
        if plateau[emplacement[0]][emplacement[1] - i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    # on ajoute à nb_pieces_alignees le nombre de pièces de la couleur de piece
    # qui y sont collées à DROITE
    for i in range(1, min(3, len(plateau[0]) - emplacement[1] - 1) + 1):
        if plateau[emplacement[0]][emplacement[1] + i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    if nb_pieces_alignees >= 4:
        return True
    else:
        nb_pieces_alignees = 1

    # diagonale haut gauche / bas droite
    for i in range(1, min(emplacement[0], emplacement[1]) + 1):
        if plateau[emplacement[0] - i][emplacement[1] - i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    for i in range(1, min(len(plateau) - emplacement[0] - 1, len(plateau[0]) - emplacement[1] - 1) + 1):
        if plateau[emplacement[0] + i][emplacement[1] + i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    if nb_pieces_alignees >= 4:
        return True
    else:
        nb_pieces_alignees = 1
    
    # diagonale haut droite / bas gauche
    for i in range(1, min(len(plateau) - emplacement[0] - 1, emplacement[1]) + 1):
        if plateau[emplacement[0] + i][emplacement[1] - i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    for i in range(1, min(emplacement[0], len(plateau[0]) - emplacement[1] - 1) + 1):
        if plateau[emplacement[0] - i][emplacement[1] + i] == piece:
            nb_pieces_alignees += 1
        else:
            break
    if nb_pieces_alignees >= 4:
        return True
    else:
        nb_pieces_alignees = 1
    return False


def plateau_plein(plateau):
    return all(cellule != ' ' for ligne in plateau for cellule in ligne)


def minimax(plateau_simule, piece, profondeur, alpha, beta):
    if est_gagnant_minimax(plateau_simule, "O"):
        # print("gagnant", piece, profondeur)
        
        return profondeur, None
    elif est_gagnant_minimax(plateau_simule, "X"):
        # print("gagnant", piece, profondeur)
        
        return -profondeur, None
    if profondeur == 0 or plateau_plein(plateau_simule):
        
        # print("joue")
        return [0, None]
    if piece == "O":
        meilleure_colonne = 0
        meilleur_score = -numpy.inf
        liste_scores = []
        pas_de_meilleur_score = True
        for i in range(0, len(plateau_simule[0])):
            if(coup_valide(plateau_simule, i)):
                stocker_piece(plateau_simule, i, "O")
                score = minimax(copy.deepcopy(plateau_simule), "X", profondeur - 1, alpha, beta)[0]
                plateau_simule[obtenir_ligne(plateau_simule, i) + 1][i] = " "
                # if score != 0:
                #     print(score)
                if meilleur_score < score:
                    meilleur_score = score
                    meilleure_colonne = i
                liste_scores.append([score, i])
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        for i in range(len(liste_scores) - 1):
            if liste_scores[i][0] != liste_scores[i + 1][0]:
                pas_de_meilleur_score = False
                break
        if pas_de_meilleur_score:
            return liste_scores[0][0], random.choice(liste_scores)[1]
        return meilleur_score, meilleure_colonne
    else:
        pire_colonne = 0
        pire_score = numpy.inf
        liste_scores = []
        pas_de_pire_score = True
        for i in range(0, len(plateau_simule[0])):
            if(coup_valide(plateau_simule, i)):
                stocker_piece(plateau_simule, i, "X")
                score = minimax(copy.deepcopy(plateau_simule), "O", profondeur - 1, alpha, beta)[0]
                plateau_simule[obtenir_ligne(plateau_simule, i) + 1][i] = " "
                if pire_score > score:
                    pire_score = score
                    pire_colonne = i
                liste_scores.append([score, i])
                beta = min(beta, score)
                if beta <= alpha:
                    break
        for i in range(len(liste_scores) - 1):
            if liste_scores[i][0] != liste_scores[i + 1][0]:
                pas_de_pire_score = False
                break
        if pas_de_pire_score:
            return liste_scores[0][0], random.choice(liste_scores)[1]
        return pire_score, pire_colonne