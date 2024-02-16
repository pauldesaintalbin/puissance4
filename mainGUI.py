# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 08:13:58 2024

@author: theo.drumme
"""

from tkinter import *
from moteur import *
import threading

COULEUR_ARRIERE_PLAN = '#EACDFF'
COULEUR_JETON_ROUGE = "#FF0000"
COULEUR_JETON_JAUNE = "#CDD12C"
COULEUR_JETON_ROUGE_GAGNANT = "#AF0000"
COULEUR_JETON_JAUNE_GAGNANT = "#C2BB00"

window = Tk()
window.title('Puissance 4')
window.geometry('1000x800')
window.minsize(500, 300)
window.iconbitmap("image/logo.ico")
window.config(background=COULEUR_ARRIERE_PLAN)




label_title= Label(window, text="Puissance 4", font=("Arial", 40),  bg=COULEUR_ARRIERE_PLAN)
label_title.pack()



#ajout texte
label_title=Label(window, text="Règle du jeu :", font=("arial", 20), bg=COULEUR_ARRIERE_PLAN)
label_title.place(x=15,y=100)

#deuxieme texte
label_subtitle1=Label(window, text="Le but du jeu est d'aligner 4 jetons de sa couleur, horizontalement, verticalement ou en diagonale, avant son adversaire.", font=("arial", 12), bg=COULEUR_ARRIERE_PLAN)
label_subtitle1.place(x=15,y=140)
label_subtitle2=Label(window, text="Le jeu se joue à deux, avec un plateau de 42 emplacements répartis en 6 lignes et 7 colonnes, et 42 jetons de 2 couleurs différentes.", font=("arial", 12), bg=COULEUR_ARRIERE_PLAN)
label_subtitle2.place(x=15,y=170)
label_subtitle3=Label(window, text="Chaque joueur, à tour de rôle, choisit une colonne et y place un de ses jetons. Le jeton tombe en bas de la colonne.", font=("arial", 12), bg=COULEUR_ARRIERE_PLAN)
label_subtitle3.place(x=15,y=200)
label_subtitle4=Label(window, text="La partie se termine quand un joueur aligne 4 jetons de sa couleur, ou quand le plateau est rempli sans alignement possible", font=("arial", 12), bg=COULEUR_ARRIERE_PLAN)
label_subtitle4.place(x=15,y=230)

    
    
# Boutons pour lancer la partie
bouton_jcj = Button(window, text = "Jouer à 2", command=lambda jcj = True, niveau_ordi = None: creer_frame_jeu(jcj, niveau_ordi))
bouton_jcj.place(x =15, y = 270)

bouton_ordinateur_facile = Button(window, text = "Jouer contre l'ordinateur - niveau facile", command=lambda  jcj = False, niveau_ordi = 5: creer_frame_jeu(jcj, niveau_ordi))
bouton_ordinateur_facile.place(x =15, y = 320)

bouton_ordinateur_moyen = Button(window, text = "Jouer contre l'ordinateur - niveau moyen", command=lambda  jcj = False, niveau_ordi = 7: creer_frame_jeu(jcj, niveau_ordi))
bouton_ordinateur_moyen.place(x =15, y = 370)

bouton_ordinateur_difficile = Button(window, text = "Jouer contre l'ordinateur - niveau difficile", command=lambda  jcj = False, niveau_ordi = 8: creer_frame_jeu(jcj, niveau_ordi))
bouton_ordinateur_difficile.place(x =15, y = 420)


def fin_de_partie(boutons, jcj, gagnant, texte_etat_partie, jetons_gagnants):
    """Cette fonction affiche le résultat de la partie et désactive les boutons"""
    for ligne in range(len(boutons)):
        for colonne in range(len(boutons[0])):
            boutons[ligne][colonne]["state"] = DISABLED
    if gagnant != None:             #change la couleur des jetons gagnants si un joueur a gagné
        for i in range(len(jetons_gagnants)):
            boutons[jetons_gagnants[i][0]][jetons_gagnants[i][1]]["bg"] = COULEUR_JETON_JAUNE_GAGNANT if gagnant == "O" else COULEUR_JETON_ROUGE_GAGNANT
    if jcj:
        if gagnant == "X":              #si victoire du joueur 1
            texte_etat_partie["text"] = "Le joueur rouge a gagné !"
        elif gagnant == "O":            #si victoire du joueur 2
            texte_etat_partie["text"] = "Le joueur jaune a gagné !"
        else:                           #si personne n'a gagné
            texte_etat_partie["text"] = "Match nul !"
    else:
        if gagnant == "X":          #si victoire du joueur
            texte_etat_partie["text"] = "Vous avez gagné !"
        elif gagnant == "O":        #si victoire de l'ordinateur
            texte_etat_partie["text"] = "L'ordinateur a gagné !"
        else:                       #si personne n'a gagné
            texte_etat_partie["text"] = "Match nul !"
    
def placer_piece(plateau, boutons, jcj, colonne, piece_actuelle, texte_etat_partie, niveau_ordi):
    """Cette fonction sert à placer une pièce si le coup est valide et met fin à la partie 
    si le coup est gagnant"""
    if coup_valide(plateau, colonne):           #place la pièce seulement si la colonne n'est pas pleine
        stocker_piece(plateau, colonne, piece_actuelle[0])
        couleur = COULEUR_JETON_ROUGE if piece_actuelle[0] == "X" else COULEUR_JETON_JAUNE
        boutons[obtenir_ligne(plateau, colonne) + 1][colonne].configure(bg=couleur, activebackground=couleur)
        if est_gagnant(plateau, piece_actuelle[0])[0] or plateau_plein(plateau):        #fin de la partie quand un joueur gagne ou que la grille est pleine
            if plateau_plein(plateau) and not est_gagnant(plateau, piece_actuelle[0])[0]:           
                piece_actuelle[0] = None 
            fin_de_partie(boutons, jcj, piece_actuelle[0], texte_etat_partie, est_gagnant(plateau, piece_actuelle[0])[1])
        else:
            if jcj: # si le mode de jeu est joueur contre joueur, c'est à l'autre joueur de jouer
                piece_actuelle[0] = "X" if piece_actuelle[0] == "O" else "O"
                texte_etat_partie["text"] = "Au tour de rouge" if piece_actuelle[0] == "X" else "Au tour de jaune"
            else: # sinon l'ordinateur joue
                #on empêche le joueur de jouer pendant que l'ordinateur réfléchit
                texte_etat_partie["text"] = "L'ordinateur réfléchit..."
                for ligne in range(len(boutons)):
                    for colonne in range(len(boutons[0])):
                        boutons[ligne][colonne]["state"] = DISABLED
                threading.Thread(target=lambda plateau = plateau, boutons = boutons:
                    ordinateur_placer_piece(plateau, boutons, texte_etat_partie, niveau_ordi)).start()
    
def ordinateur_placer_piece(plateau, boutons, texte_etat_partie, niveau_ordi):
    """Cette fonction appelle l'ordinateur pour qu'il place une pièce et met fin à la partie
    si son coup est gagnant"""
    colonne_ordi = minimax(copy.deepcopy(plateau), "O", niveau_ordi, -numpy.inf, numpy.inf)[1]
    stocker_piece(plateau, colonne_ordi, "O")
    boutons[obtenir_ligne(plateau, colonne_ordi) + 1][colonne_ordi].configure(bg = COULEUR_JETON_JAUNE)
    for ligne in range(len(boutons)):
        for colonne in range(len(boutons[0])):
            boutons[ligne][colonne]["state"] = NORMAL
    texte_etat_partie["text"] = "À vous de jouer"
    if est_gagnant(plateau, "O")[0]:        #fin de la partie quand l'ordinateur gagne
        fin_de_partie(boutons, False, "O", texte_etat_partie, est_gagnant(plateau, "O")[1])
    elif plateau_plein(plateau):            #fin de la partie quand la grille est pleine
        fin_de_partie(boutons, False, None, texte_etat_partie, est_gagnant(plateau, "O")[1])

#création d'une nouvelle fenetre   
def creer_frame_jeu(joueur_contre_joueur, niveau_ordi = None):
    """Cette fonction sert à créer une nouvelle interface de jeu avec la grille de jeu et quel joueur
    doit jouer"""
    piece_actuelle = ["X"] # Cette variable contient le joueur à qui c'est le tour, 
    # stockée dans un tableau pour que lorsqu'on modifie extérieurement sa valeur, 
    # cette fonction puisse y accéder (les modifications des éléments de tableaux 
    # sont globales en python)
    jcj = joueur_contre_joueur
    plateau = initialiser_plateau(6, 7)
    win = Tk()
    win.title('Grille de jeu')
    win.geometry('900x500')
    win.config(bg=COULEUR_ARRIERE_PLAN)
    texte_etat_partie = Label(win, text="Au tour de rouge" if jcj else "À vous de jouer", font=("arial", 15), bg=COULEUR_ARRIERE_PLAN)
    texte_etat_partie.pack()
    frame_jeu = Frame(win)
    
    #création de la grille et des boutons
    boutons = []
    for ligne in range(len(plateau)):
        ligne_boutons = []
        for colonne in range(len(plateau[0])):
            bouton=Button(frame_jeu, bg=COULEUR_ARRIERE_PLAN, activebackground=COULEUR_ARRIERE_PLAN)
            bouton.grid(row=ligne, column=colonne, sticky='ew',ipadx=30, ipady=20)
            ligne_boutons.append(bouton)
        boutons.append(ligne_boutons)
    # Ajout de l'événement au clic d'un bouton
    for ligne in range(len(boutons)):
        for colonne in range(len(boutons[0])):
            boutons[ligne][colonne]["command"] = lambda colonne = colonne, plateau = plateau, piece_actuelle = piece_actuelle, texte_etat_partie = texte_etat_partie: placer_piece(plateau, boutons, jcj, colonne, piece_actuelle, texte_etat_partie, niveau_ordi)
    frame_jeu.pack(expand=True) 
    #Affiche la fenêtre de jeu
    win.mainloop()
   




#Affiche la fenêtre principale
window.mainloop()
