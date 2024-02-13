from tkinter import *
from moteur import *


window = Tk()
window.title('Puissance 4')
window.geometry('1000x800')
window.minsize(500, 300)
window.iconbitmap("jeton/logo.ico")
window.config(background='#2cdf85')


frame = Frame(window, bg="", bd=1, relief=SUNKEN)

label_title= Label(window, text="Puissance 4", font=("Arial", 40), background='red')
label_title.pack()

frame.pack(expand=YES)

#ajout texte
label_title=Label(window, text="Règle du jeu:", font=("arial", 20), bg="#2cdf85")
label_title.place(x=15,y=100)

#deuxieme texte
label_subtitle=Label(window, text="_Le but du jeu est d'aligner 4 jetons de sa couleur, horizontalement, verticalement ou en diagonale, avant son adversaire.", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=140)
label_subtitle=Label(window, text="_Le jeu se joue à deux, avec un plateau de 42 emplacements répartis en 6 lignes et 7 colonnes, et 42 jetons de 2 couleurs différentes.", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=170)
label_subtitle=Label(window, text="_Chaque joueur, à tour de rôle, choisit une colonne et y place un de ses jetons. Le jeton tombe en bas de la colonne.", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=200)
label_subtitle=Label(window, text="_La partie se termine quand un joueur aligne 4 jetons de sa couleur, ou quand le plateau est rempli sans alignement possible", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=230)

label_subtitle=Label(window, text="Entrez votre nom de joueur:", font=("arial", 12), bg="#2cdf85")
label_subtitle.place(x=15,y=300)
myEntry = Entry(window, width=20)
myEntry.place(x=210,y=303)

# mettre une image
from PIL import ImageTk,Image
img = ImageTk.PhotoImage(Image.open("jeton/logo.ico"))
panel = Label(window, image = img, bg="#2cdf85")
panel.place(x=15,y=400)

nombre_lignes=6
nombre_colonnes=7
plateau = [[' ' for i in range(nombre_colonnes)] for i_n in range(nombre_lignes)]  

#création d'une nouvelle fenetre   
def create():
    win = Tk()
    win.title('Grille de jeu')
    win.geometry('400x300')
    win.config(bg='blue')

    frame = Frame(win, bg='#F2B33D')
    piece='X'
    for i in range(nombre_lignes):
        for a in range(nombre_colonnes):
            b2=Button(frame,command=changer_couleur)
            b2.grid(row=i, column=a, sticky='ew',ipadx=15, ipady=10)
            
    frame.pack(expand=True) 
    
    win.mainloop()
   


def update_board():
    for i in range(6):
        for j in range(7):
            if plateau[i, j] == 'X':
                plateau[i][j].configure(text='', bg='yellow', relief='sunken', state='disabled')
            elif plateau[i, j] == '0':
                plateau[i][j].configure(text='', bg='red', relief='sunken', state='disabled')
    
# bouton cliquable
b1 = Button(window, text = "Commencer la partie",command=create)
b1.place(relx = 1, x =-300, y = 300, anchor = NE)






#Afficher la fenetre
window.mainloop()






   

   


