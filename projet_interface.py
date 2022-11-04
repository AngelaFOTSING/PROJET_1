from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# La fenêtre
fenetre = Tk()
fenetre.title("PKI ET PYTHON")
fenetre.geometry("1000x500")


label = Label(fenetre, relief = RIDGE, text="ANGELA'S PKI CERTIFICATE GENERATOR", font=("Times New Roman", 20), fg='black', bg = "white")
label.place(x = 0, y = 0, width = 1365)
label.pack()


####### Collecte des données #######

# Organisation/entreprise
lblentreprise = Label(fenetre, text = " Entreprise / Company", font = ("Arial", 12), bg = "grey", fg="white")
lblentreprise.place(x=0,y=100,width=200)
entrerentreprise = Entry(fenetre)
entrerentreprise.place(x=200,y=100,width=160,height=30)

#Pays
lblpays = Label(fenetre, text = "Pays / Country", font = ("Arial", 12), bg = "grey", fg="white")
lblpays.place(x=0,y=150,width=200)
entrerpays = Entry(fenetre)
entrerpays.place(x=200,y=150,width=200,height=30)

#Ville
lblville = Label(fenetre, text = "Ville / City", font = ("Arial", 12), bg = "grey", fg="white")
lblville.place(x=0,y=200,width=200)
entrerville= Entry(fenetre)
entrerville.place(x=200,y=200,width=200,height=30)



 

o = ttk.Combobox (fenetre, values=["SHA", "SHA1", "SHA256", "SHA512"])
o.pack ()


        #print(o.get())
        #age = entrerage.get()
        
def algorithme() :                    
    print(o.get())
        
bout = Button(fenetre, text="Algorithme de chiffrement")
bout.config (command = algorithme)        
bout.pack ()
#def print_file () :                     # voir le chapitre sur les événements
    #print(o.get())



#b = tkinter.Button (root, text="print")
#b.config (command = print_file)         # idem
#b.pack ()


#b=Button(fenetre, text="Fermer", command=fenetre.save)
#b.pack()
def enregistrer():
        entreprise = entrerentreprise.get()
        label.configure(text=entreprise)
        print(entreprise)
        pays = entrerpays.get()
        label.configure(text=pays)
        print(pays)
        ville = entrerville.get()
        label.configure(text=ville)
        print(ville)
       
        
#btn =Button(fenetre, height=1, width=10, text="Enregistrer", command=save_info)
#btn.pack(pady=20)    

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()