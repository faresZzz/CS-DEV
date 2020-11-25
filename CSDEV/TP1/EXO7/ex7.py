
import time
def amicaux(nb1,nb2):
    diviseur1=diviseur(nb1)
    diviseur2=diviseur(nb2)
    
    
    if sum(diviseur1) == sum(diviseur2) ==  nb1+nb2:
        return True
    return False

def diviseur(nombre):
    divi=[]
    for i in range (1,nombre+1):
        if nombre % i == 0:
            divi.append(i)
    return divi

def tous_les_amicaux(N):
    liste=[]
    for i in range(1,N+1):
        for k in range(1,N+1):
            if i !=k:
                if amicaux(i,k) :
                    liste.append([i,k])
    return liste

start=time.time()
print(tous_les_amicaux(100))
fin=time.time()
print(fin-start)