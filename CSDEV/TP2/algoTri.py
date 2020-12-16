
import time
import random



def triselection(li):
    # methode tri par selection
    n=len(li)
    for i in range (0,n):
        petit=li[i]
        j=i
        for k in range (i+1,n):
            if li[k]<petit:
                j=k
                petit=li[k]
        li[j], li[i] = li[i] ,li[j]
    return li

def tirBulle(li):
    # methode tribule
    for i in range (len(li)-1):
        for j in range (len(li)-1-i):
            if li[j]>li[j+1]:
                li[j], li[j+1]= li[j+1], li[j]
    
    return li

def tirBulle2(li):
    # methode tribule
    permutation=True
    while permutation:
        permutation=False
        for j in range (len(li)-1):
            if li[j]>li[j+1]:
                li[j], li[j+1]= li[j+1], li[j]
                permutation=True
    
    return li

def tri_Insertion(li):
    n=len(li)
    for i in range(1,n):
        k=li[i]
        j=i-1
        while j>=0 and k<li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1]=k
    
    return li

def tri_rapide(table,g,d):
    if g<d:
        v=table[g]
        m=g
        for i in range(g+1,g+1):
            if table[i] < v:
                m=m+1
                table[m],table[i]=table[i],table[m]
        tri_rapide(table,g,m-1)
        tri_rapide(table,m+1,d)




start=time.time()
N=100000
T=[random.randint(0,2*N) for _ in range(N)]
li=[1,2,3,4,5,6,7,8,9,6,4,1,5,3,6,8,1,2,4,9,2,6,5,2,3,6]



tri_rapide(T,T[0],T[-1])
stop=time.time()
print(stop-start)