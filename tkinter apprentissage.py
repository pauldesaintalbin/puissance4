from tkinter import *

window = Tk()
window.title('Puissance 4')
window.geometry('1000x800')
window.minsize(500, 300)
window.iconbitmap("../image/logo.ico")

frame = Frame(window, bg="#ff0000", bd=1, relief=SUNKEN)

label_title= Label(window, text="Puissance 4", font=("Arial", 40))
label_title.pack()

frame.pack(expand=YES)
#Afficher la fenetre
window.mainloop()
