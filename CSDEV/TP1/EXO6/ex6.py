

def tricolore(n):
    carreParfait=["1","4","9"]
    nb=n*n
    for chiffre in str(nb):
        if chiffre not in carreParfait:
            return False
    return True


def tous_les_tricolore(N):
    trico=[]
    for i in range(N+1):
        if tricolore(i):
            trico.append(i)
    return(trico)
print(tous_les_tricolore(100000))