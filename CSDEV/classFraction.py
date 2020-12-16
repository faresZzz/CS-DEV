class Fraction:
    def __init__(self,num,denom):
        self.numerateur=num
        self.denominateur=denom
    
    def __add__(self,vect):
        if vect.isinstance(Fraction):
            deno=self.denominateur*vect.denominateur
            num=(self.numerateur*vect.denominateur+vect.numerateur*self.denominateur
            return (str(num/pgcd(num,deno))+"/"+str(deno/pgcd(num,deno)))
        else:
            return "probeleme de classe"










def pgcd(a,b):
    while b!=0:
        a=b
        b=a%b
    return a