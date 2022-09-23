import math
import matplotlib.pyplot as plt

class ed_curves:
    def __init__(self,a,d,p):
        self.a = a
        self.d = d
        self.p = p
        
    def gcd(a,b):
            if a == 0 or b==0:
                if a + b == 0:
                    print('GCD does not exist')
                else:
                    return a + b
            else:
                return ed_curves.gcd(b%a,a)
            
    def prime_check(n):
            if n<=1:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if ed_curves.gcd(n,i)==1:
                    continue
                else:
                    return False
            return True
        
    def mod_inverse(n,p):
        if ed_curves.prime_check(p):
            for i in range(1,p):
                if (i*n)%p==1:
                    return i
        else:
            return str(p)+' is not prime.'
    
    def curve_plot(self):
        if ed_curves.prime_check(self.p) and self.a*self.d*(self.a-self.d)!=0:
            C = []
            if ed_curves.prime_check(self.p):
                for i in range(1,self.p):
                    for j in range(1,self.p):
                        if (self.a*pow(i,2)+pow(j,2)-1-self.d*pow(i,2)*pow(j,2))%self.p==0:
                            C.append((i,j))
            if len(C)!=0:
                plt.scatter(*zip(*C),s=10)
            
            plt.title(f'Points lying on twisted edwards curve with {self.a}$x^2$ + $y^2$= 1 + {self.d}$x^2y^2$ over $F_{{p}}$( p = {self.p})')
            return C
        
        else:   
            return []
    
    def check_point(self,P):
        if ed_curves.prime_check(self.p) and self.a*self.d*(self.a-self.d)!=0:
            if len(P[0])==1:
                x = int(P[0][0])%self.p
                if len(P[1])==1:
                    y = int(P[1][0])%self.p
                    if (x,y) in ed_curves.curve_plot(self):
                        return True
                    else:
                        return False
                else:
                    nu = int(P[1][0])%self.p
                    de = int(P[1][1])%self.p
                    if ed_curves.gcd(d,self.p)==1:
                        y = (nu*ed_curves.mod_inverse(de,self.p))%self.p
                        if (x,y) in ed_curves.curve_plot(self):
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                nu = int(P[0][0])%self.p
                de = int(P[0][1])%self.p
                if ed_curves.gcd(de,self.p)==1:
                    x = (nu*ed_curves.mod_inverse(de,self.p))%self.p
                    if len(P[1])==1:
                        y = int(P[1][0])%self.p
                        if (x,y) in ed_curves.curve_plot(self):
                            return True
                        else:
                            return False
                    else:
                        nu = int(P[1][0])%self.p
                        de = int(P[1][1])%self.p
                        if ed_curves.gcd(d,self.p)==1:
                            y = (nu*ed_curves.mod_inverse(de,self.p))%self.p
                            if (x,y) in ed_curves.curve_plot(self):
                                return True
                            else:
                                return False
                        else:
                            False
                else:
                    return False
        else:
            return False
        
          
if __name__=='__main__':
    a = int(input('Enter a - '))
    d = int(input('Enter d - '))
    p = int(input('Enter prime - '))
    obj = ed_curves(a,d,p)
    print('Points on twisted edwards curve - ',obj.curve_plot())
    P = []
    for _ in range(2):    
        x = tuple(input().split('/'))
        P.append(x)
    print(obj.check_point(P))
    
            