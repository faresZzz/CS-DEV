"""
fichier principale mode graphique
realiser par fares zaghouane le 08/12/20
https://github.com/faresZzz/CS-DEV
TO Do ajouter la possibiliter de recommancer la partie et mettre en forme la page pour que ca soit joli
"""


import tkinter
import modGra

 




def essai(img,aff,lettre,utilisé ,dejU):
    #function qui s'active des que l'utilisateur entre une lettre 
    # gere la partie avec l'affichage des lettre et de l'image
    valide=modGra.dejeUtiliser(lettre.get(),partie.teste)
    if valide:
        affichage,partie.valides,partie.teste,partie.vie=modGra.Correspondance(partie.mot,lettre.get(),partie.valides,partie.teste,partie.vie)
        img.configure(file="../images/bonhomme"+str(partie.vie)+".gif")
        aff.configure(text = affichage)
        
        Fin( img,aff ,lettre)
    else:
        dejU.configure(text="Cette lettre a deja ete dite")
        
    lettre.delete(0,"end")  
    utilisé.configure(text="lettres deja utilisée"+str(partie.teste[1:]))

def Fin( image,affichage,lt):
    #gere la fin de partie en ouveant une nouvelle fenetre ou l'utilisateur
    # doit selectionner s'il veux recommancer ou non (fonctionne pas bien) 
    partie.continuer,gagner=modGra.FinDEPArtie(partie.vie,partie.mot,partie.valides)

    if partie.continuer==False:
        new=tkinter.Toplevel(fenetre)
       
        if gagner:
            result=tkinter.Label(new,text="bravo vous avez gagner")
        else:
            result=tkinter.Label(new,text="dommage vous avez perdu")
        
        v=tkinter.StringVar()    
        again=tkinter.Label(new,text="Voulez-vous Recommencer" )
        recommencer=tkinter.Radiobutton(new,text="oui" ,value="1", variable=v)
        quitter=tkinter.Radiobutton(new,text="non" , value="0" ,variable=v) 
        ok=tkinter.Button(new,text="entrer",command=lambda:nouveau(v,new, image,affichage ,lt))
        again.pack()
        recommencer.pack()
        quitter.pack()
        ok.pack()
        result.pack()
       
        
def nouveau(value ,newWindow, image,affiche ,lettr):
    # reinitionlise la partie si l'utilisateur veuc recommencer 
    # sinon ferme les fenetres
    if value=='0':
        aurevoir=tkinter.Label(newWindow,text="merci aurevoir")
        aurevoir.pack()
        newWindow.destroy()
        fenetre.destroy()
    else:
        newWindow.destroy()
       
        partie.vie=8
        partie.mot=modGra.Mot(modGra.lectureDoc())
        partie.valide=[]
        partie.teste=[]
        partie.continuer=True 
        image.configure(file="../images/bonhomme"+str(partie.vie)+".gif")
        #essai(image,affiche,lettr,)
        





# ----- Programme principal : -----


document=modGra.lectureDoc()
motADeviner=modGra.Mot(document)
print(motADeviner)
partie=modGra.Partie(motADeviner)

affiche,partie.valides,partie.teste,partie.vie=modGra.Correspondance(partie.mot,motADeviner[0],partie.valides,partie.teste,partie.vie)

fenetre =tkinter.Tk()
entree = tkinter.Entry(fenetre)

chaine = tkinter.Label(fenetre,text=affiche)

photo=tkinter.PhotoImage(file="../images/bonhomme"+str(partie.vie)+".gif")
largeur=500
hauteur=500
canvas=tkinter.Canvas(fenetre, width=largeur , height=hauteur, bg="#3c3e43" )
imag=canvas.create_image(0,0,anchor='nw' , image=photo)
listeU=tkinter.Label(fenetre)
dejU=tkinter.Label(fenetre)

btn=tkinter.Button(fenetre,text="soumettre", fg='blue', command=lambda:[essai(photo,chaine,entree,listeU,dejU)])
entree.pack()
btn.pack()
chaine.pack()
canvas.pack() 
listeU.pack()
dejU.pack()    
fenetre.mainloop()