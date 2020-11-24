

def multiplication(matriceA,matriceB):
    matriceC=[]
    if len(matriceA) == len(matriceB[0]):
        for i in range (len(matriceA)):
            vecteur=[]
            for j in range(len(matriceB[0])):
                val=0
                for k in range (len(matriceA[0])):
                    val+=matriceA[i][k]*matriceB[k][j]
                vecteur.append(val)
            matriceC.append(vecteur)
    else:
        return "probleme de dimension"
    return affichage(matriceC)



def affichage(matice):
    for val in matice:
        print(val)


A=[[1,0,0],[0,1,0],[0,0,1]]
B=[[2,1,0],[-5,1,0],[4,0,0]]
print(multiplication(A,A))