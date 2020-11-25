
def syracus(nb,altitude,vol):
    
    if nb > altitude:
        altitude= nb
    while nb !=1:
        if nb %2 == 0:
            
            return syracus(nb/2,altitude,vol+1)
            
        else:
            return syracus(3*nb+1,altitude,vol+1)

    return (altitude,vol)
    


        

def compet(n):
    maxpplus=[]
    volplus=[]
    for val in range(1,n+1):
        m,v=syracus(val,0,0)
        maxpplus.append([val,m])
        volplus.append([val,v])
    
    return (maxpplus,volplus)

def resul(nb):    
    mmax=[0,0]
    vol=[0,0]
    listemax,listevol=compet(nb)
    for val in ( listemax):
        if val[1]>mmax[1]:
            mmax=val

    for vl in(listevol):
        if vl[1]>vol[1]:
            vol=vl

    print(mmax)
    print(vol)

resul(100)