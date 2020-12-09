"""
module qui nous sert pour la partie console ou l'on a toutes les fonctions du jeu.
realiser par fares zaghouane 01/12/20


"""


import random


def lectureDoc():
    #function qui vas lire le fichier avec les mots et nous ressortir une liste de mot
    fichier=open("../bankdeMot.txt","r", encoding="utf8")
    listMOt=fichier.readlines()
    fichier.close()
    for i in range(len(listMOt)):
        listMOt[i]=listMOt[i].rstrip("\n")

    return listMOt

def Mot(listeMot):
    #fonction qui vas recupere une mot au hazard dans la liste et nous le redonner sour forme de liste
    corresp={"è":"e","é":"e","â":"a","ê":"e","ï":"i"}
    i=random.randint(0, len(listeMot))
    choix=listeMot[i]
    lettre=[]
    for lt in choix:
        if lt in corresp:
            lettre.append(corresp[lt])
        else:
            lettre.append(lt)
    return lettre

def Affichage(mot, lettreDevine):
     #fonction qui permet de gerer si l'on afficher une lettre ou un tiret
    for lettre in mot:
        if lettre in lettreDevine:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print('')


def Utilisateur():
    #function qui gere la saisie de lettre par l'utilisateur
    lettreUtilisateur=input("choisir une lettre: ")

    return lettreUtilisateur.lower()


def Correspondance(motDevine,testUtilisateur,Dites , compteur):
    # fonction pricipale du jeu qui determine si la llettre de l'utilisateur est bien dans le mot et gere la vie
    # retourne la liste des lettre valides la liste des lettres utiliser le vie les lettre a afficher
    if testUtilisateur in motDevine:
        occurence= motDevine.count(testUtilisateur)
        for i in range(occurence):
            Dites.append(testUtilisateur)

        Affichage(motDevine,Dites)

    else:
        compteur=compteur-1
        Affichage(motDevine,Dites)
        print("il vous reste: ",compteur,' vies')
    return Dites, compteur

def FinDEPArtie(vie,motadeviner,lettreDejaDevine):
    #fonction qui gere si la partie est finie ou non
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motadeviner)== len(lettreDejaDevine):
        valRen=False
        print("bien joué")
    return valRen   

