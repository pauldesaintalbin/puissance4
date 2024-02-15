# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:35:37 2024

@author: PC ASUS
"""

from tkinter import *
from moteur import *
from random import *
import threading

window = Tk()
window.title('Puissance 4')
window.geometry('1000x800')
window.minsize(500, 300)
# window.iconbitmap("jeton/logo.ico")
window.config(background='#2cdf85')


frame = Frame(window, bg="", bd=1, relief=SUNKEN)

label_title= Label(window, text="Puissance 4", font=("Arial", 40), background='red')
label_title.pack()

frame.pack(expand=YES)

#ajout texte
label_title=Label(window, text="Règle du jeu:", font=("arial", 20), bg="#2cdf85")
label_title.place(x=15,y=100)

#deuxieme texte
label_subtitle1=Label(window, text="_Le but du jeu est d'aligner 4 jetons de sa couleur, horizontalement, verticalement ou en diagonale, avant son adversaire.", font=("arial", 12), bg="#2cdf85")
label_subtitle1.place(x=15,y=140)
label_subtitle2=Label(window, text="_Le jeu se joue à deux, avec un plateau de 42 emplacements répartis en 6 lignes et 7 colonnes, et 42 jetons de 2 couleurs différentes.", font=("arial", 12), bg="#2cdf85")
label_subtitle2.place(x=15,y=170)
label_subtitle3=Label(window, text="_Chaque joueur, à tour de rôle, choisit une colonne et y place un de ses jetons. Le jeton tombe en bas de la colonne.", font=("arial", 12), bg="#2cdf85")
label_subtitle3.place(x=15,y=200)
label_subtitle4=Label(window, text="_La partie se termine quand un joueur aligne 4 jetons de sa couleur, ou quand le plateau est rempli sans alignement possible", font=("arial", 12), bg="#2cdf85")
label_subtitle4.place(x=15,y=230)

label_subtitle=Label(window, text="Entrez votre nom de joueur:", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=300)
myEntry = Entry(window, width=20)
myEntry.place(x=210,y=303)

# mettre une image
# from PIL import ImageTk,Image
# img = ImageTk.PhotoImage(Image.open("jeton/logo.ico"))
# panel = Label(window, image = img, bg="#2cdf85")
# panel.place(x=15,y=400)


    
def placer_piece(plateau, boutons, jcj, colonne, piece_actuelle):
    # global piece_actuelle
    if coup_valide(plateau, colonne):
        stocker_piece(plateau, colonne, piece_actuelle[0])
        couleur = "red" if piece_actuelle[0] == "X" else "yellow"
        boutons[obtenir_ligne(plateau, colonne) + 1][colonne].configure(bg=couleur)
        print("piece posee")
        if est_gagnant(plateau, piece_actuelle[0], [obtenir_ligne(plateau, colonne) + 1, colonne]):
            if couleur=="red":
                messagebox.showinfo("Victoire", f"Victoire de rouge !")
            else:
                messagebox.showinfo("Victoire", f"Victoire de jaune !")
            for ligne in range(len(boutons)):
                for colonne in range(len(boutons[0])):
                    boutons[ligne][colonne]["state"] = DISABLED
        if jcj: # si le mode de jeu est joueur contre joueur, c'est à l'autre joueur de jouer
            piece_actuelle[0] = "X" if piece_actuelle[0] == "O" else "O"
        else: # sinon l'ordinateur joue
            #on empêche le joueur de jouer pendant que l'ordinateur réfléchis
            for ligne in range(len(boutons)):
                for colonne in range(len(boutons[0])):
                    boutons[ligne][colonne]["state"] = DISABLED
            threading.Thread(target=lambda plateau = plateau, boutons = boutons:
                ordinateur_placer_piece(plateau, boutons)).start()
    
def ordinateur_placer_piece(plateau, boutons):
    print("sqdfglsqdgkj")
    colonne_ordi = minimax(copy.deepcopy(plateau), "O", 8, -numpy.inf, numpy.inf)[1]
    print("ordi :", colonne_ordi)
    stocker_piece(plateau, colonne_ordi, "O")
    boutons[obtenir_ligne(plateau, colonne_ordi) + 1][colonne_ordi].configure(bg="yellow")
    for ligne in range(len(boutons)):
        for colonne in range(len(boutons[0])):
            boutons[ligne][colonne]["state"] = NORMAL
    if est_gagnant(plateau, "O", [obtenir_ligne(plateau, colonne_ordi) + 1, colonne_ordi]):
            messagebox.showinfo("Victoire", f"Victoire de l'ordi !")
            print("gagnant")
            for ligne in range(len(boutons)):
                for colonne in range(len(boutons[0])):
                    boutons[ligne][colonne]["state"] = DISABLED

#création d'une nouvelle fenetre   
def creer_frame_jeu(joueur_contre_joueur):
    # global piece_actuelle
    piece_actuelle = ["X"] # Cette variable contient le joueur à qui c'est le tour, 
    # stockée dans un tableau pour que lorsqu'on modifie extérieurement sa valeur, 
    # cette fonction puisse y accéder (les modifications des éléments de tableaux 
    # sont globales en python)
    jcj = True if joueur_contre_joueur else False
    plateau = initialiser_plateau(6, 7)
    win = Tk()
    win.title('Grille de jeu')
    win.geometry('400x300')
    win.config(bg='blue')

    frame_jeu = Frame(win, bg='#F2B33D')
    
    boutons = []
    for ligne in range(len(plateau)):
        ligne_boutons = []
        for colonne in range(len(plateau[0])):
            bouton=Button(frame_jeu)
            bouton.grid(row=ligne, column=colonne, sticky='ew',ipadx=15, ipady=10)
            ligne_boutons.append(bouton)
        boutons.append(ligne_boutons)
    # Ajout de l'événement au clic d'un bouton
    for ligne in range(len(boutons)):
        for colonne in range(len(boutons[0])):
            boutons[ligne][colonne]["command"] = lambda colonne = colonne, plateau = plateau, piece_actuelle = piece_actuelle: placer_piece(plateau, boutons, jcj, colonne, piece_actuelle)
    frame_jeu.pack(expand=True) 
    
    win.mainloop()
   



    
    
# bouton cliquable
b1 = Button(window, text = "Jouer à 2", command=lambda jcj = True: creer_frame_jeu(jcj))
b1.place(relx = 1, x =-300, y = 300, anchor = NE)

b2 = Button(window, text = "Jouer contre l'ordinateur", command=lambda  jcj = False: creer_frame_jeu(jcj))
b2.place(relx = 1, x =-300, y = 350, anchor = NE)






#Afficher la fenetre
window.mainloop()