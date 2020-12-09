"""
module qui nous sert pour la partie graphique ou l'on a toutes les fonctions du jeu.
realiser par fares zaghouane 08/12/20


"""


import random


class Partie:
    #classe partie qui contient tous les attribut necessaire a chaque partie
    def __init__(self,motADeviner,lettresValides=[],lettresTestes=[],vie=8,continuer=True):
        self.mot=motADeviner
        self.valides=lettresValides
        self.teste=lettresTestes
        self.vie=vie
        self.continuer=continuer

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
    #fonction qui permet de gerer si l'on afficher une lettre ou un tiret ressort une liste
    valren=[]
    for lettre in mot:
        if lettre in lettreDevine:
            valren.append(lettre)
        else:
            valren.append("_")
    return valren


def Correspondance(mot,testUtilisateur,valides ,testes, compteur):

    # fonction pricipale du jeu qui determine si la llettre de l'utilisateur est bien dans le mot et gere la vie
    # retourne la liste des lettre valides la liste des lettres utiliser le vie les lettre a afficher
    testes.append(testUtilisateur)
    aAfficher=[]
    if testUtilisateur in mot:
        occurence= mot.count(testUtilisateur)
        for i in range(occurence):
            valides.append(testUtilisateur)

        aAfficher= Affichage(mot,valides)

    else:
        compteur=compteur-1
        aAfficher=Affichage(mot,valides)
        print("il vous reste: ",compteur,' vies')
    return aAfficher,valides,testes, compteur


def dejeUtiliser(nouvelleLettre,testes):
    #fonction qui verifier si une lettre a deja ete dite par l'utilisateur
    valide=True
    if nouvelleLettre in testes:
        valide=False
    return valide

def FinDEPArtie(vie,motadeviner,lettreDejaDevine):
    #fonction qui gere si la partie est finie ou non
    valRen=True
    gagner=True
    if vie==1:
        valRen= False
        gagner=False
    elif len(motadeviner)== len(lettreDejaDevine):
        valRen=False
        
    return valRen,gagner 

