"""
fichier principale du jeu mode console 
realiser par fares zaghouane le 01/12/20
https://github.com/faresZzz/CS-DEV

"""
import modCons

partie=True
meilleurScore=0

while partie:
    #boucle principale du jeu
    vie=8
    dejaDevine=[]
    continuer=True
    document=modCons.lectureDoc()
    toutesLettres=[]
    motADeviner=modCons.Mot(document)

    dejaDevine, vie=modCons.Correspondance(motADeviner,motADeviner[0], dejaDevine, vie)

    print(motADeviner)

    while continuer:
        #boucle principale de la partie
        testU=modCons.Utilisateur()
        if testU not in toutesLettres:
            toutesLettres.append(testU)
            dejaDevine, vie =modCons.Correspondance(motADeviner,testU, dejaDevine, vie)
            continuer=modCons.FinDEPArtie(vie,motADeviner,dejaDevine)
            print(toutesLettres)
        else:
            print("la lettre a deja ete dite")  
            print(toutesLettres) 

    if vie> meilleurScore:
        meilleurScore=vie

    print("c'est fini")

    nouvellePartie=input('voulez vous recommencer:(o/n): ')
    if nouvellePartie.lower()=="n":
        partie=False  

print("merci bye")


