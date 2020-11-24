
def Bisextile(annee):
    year=int(annee)
    if (year % 4 == 0  and year % 100 !=0)   or (year % 400 == 0):
        return True
    else:
        return False

def nbJours(mo, an):
    mois31=[ 1, 3, 5, 7, 8, 10 , 12 ]
    mois=int(mo) 
    
    if mois > 12 or mois < 1 :
        return -1
    else:
        if mois == 2:
            if Bisextile(an):
                return 29
            else:
                return  28
        if mois in mois31:
            return 31 
        else:
            return 30

def dateValide(j,m, a):
    jour= int(j)
    if  jour<1 or jour >nbJours(m,a):
        return False
    else:
        return True

