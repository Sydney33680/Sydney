def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
    
def ppcm(a,b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//pgcd(a,b)



class fraction:
    def __init__(self,a,b):
        self.valeur=(a,b)
    
    def afficher(self):
        (a,b)=self.valeur
        return(str(a)+"/"+str(b))
    
    def add(self,f):
        """Fonction qui addition deux fractions et change la premiere fraction en la fraction resultante"""
        (a1,b1)=self.valeur
        (a2,b2)=f.valeur
        self.valeur=(a1*b2+b1*a2,b1*b2)
        return(self)
    
    def mult(self,f):
        """de meme pour la multiplication"""
        (a1,b1)=self.valeur
        (a2,b2)=f.valeur
        self.valeur=(a1*a2,b1*b2)
        return(self)
    
    def simplifier(self):
        """fonction simplifiant la fraction"""
        (a,b)=self.valeur
        p=pgcd(a,b)
        while p!=1:
            self.valeur=(a//p,b//p)
            (a,b)=self.valeur
            p=pgcd(a,b)
        return(self)

((fraction(1,2).add(fraction(3,4))).mult(fraction(2,3))).simplifier()

def H(n):
    """Calcule le nieme terme de la série harmonique"""
    H=fraction(0,1)
    for i in range(1,n+1):
        H.add(fraction(1,i))
        H.simplifier()
    return H

def Kempner(n):
    """Calcule le nieme terme de la serie de Kempner"""
    H=fraction(0,1)
    for i in range(1,n+1):
        if not('9' in str(i)):
            H.add(fraction(1,i))
            H.simplifier()
    return H    

def Leibniz(n):
    """Calcule le nieme terme de la serie de Leibniz"""
    H=fraction(0,1)
    for i in range(1,n+1):
        m=i%2
        if m==0:
            H.add(fraction(1,2*i+1))
            H.simplifier()
        else:
            H.add(fraction(-1,2*i+1))
            H.simplifier()
    return H

H(100)
Kempner(100)
Leibniz(100)

class Polynome:
    def __init__(self,L):
        self.valeur=L
    
    def __str__(self):
        L=self.valeur
        n=len(L)
        c=''
        for i in range(n):
            if i!=(n-1):
                c+=(str(L[i])+"X^"+str(n-i-1)+"+")
            else:
                c+=(str(L[i])+"X^"+str(n-i-1))
        return c
        
    def add(self,P):
        """Additionne 2 polynomes"""
        P1=self.valeur
        P2=P.valeur
        if len(P2)>len(P1):
            n=len(P2)
            for i in range(len(P1),n):
                P1.insert(0,0)
                self.valeur=P1
        else:
            n=len(P1)
        for i in range(n):
            P1[i]+=P2[i]
        self.valeur=P1
        return(self)
    
    def deriv(self):
        P=self.valeur
        n=len(P)
        Pp=[]
        for i in range(n-1):
            Pp.append((n-1-i)*P[i])
        self.valeur=Pp
        return(self)
    
P1=Polynome([2,2,2])
P2=Polynome([1,2,3,4])
P1.add(P2)

P=Polynome.deriv(Polynome([2,2,2]))
print(P)
