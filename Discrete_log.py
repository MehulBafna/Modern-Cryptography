#Computation of discrete logarithm using baby-step-giant-step-algorithm

import math
import numpy as np

class discrete_log:
    
    def __init__(self,p,k,n):
        self.p = p
        self.k = k
        self.n = n
        
    @staticmethod
    def is_prime(n):
        if n<=1:
            return 'Invalid input'
        for i in range(2,int(math.sqrt(n))+1):
            if n%i!=0:
                continue
            else:
                return False
                break
        return True
    
    #Computing GCD
    @staticmethod
    def gcd(a,b):
        if a == 0 or b==0:
            if a + b == 0:
                return 'GCD does not exist'
            else:
                return a + b
        else:
            return discrete_log.gcd(b%a,a)
    
    #Euler Totient function  
    @staticmethod
    def euler_phi(n):  
        count = 0
        for i in range(1,n+1):
            if discrete_log.gcd(i,n)==1:
                count = count + 1
        return count

    # Computation of primitive roots
    @staticmethod
    def prim(N):
        n = abs(N)
        t = np.zeros((n-2,n-2))
        if discrete_log.is_prime(n)==False:
            return 'Primitive roots does not exist'
            
        elif discrete_log.is_prime(n)==False:
            # Creates a matrix where each row consists of (i^j)%n for j belongs to {2,...,n-1}.
            for i in range(2,n):
                for j in range(2,n):
                    x = pow(i,j,n)
                    t[i-2][j-2] = x        
            b = []  
            y = []      
            for k in range(0,n-2):
                b = t[k]      
                # Check whether cardinality of unique elements in a row is unique or not.                 
                if len(np.unique(b))==discrete_log.euler_phi(n): 
                    if discrete_log.gcd(k+1,n)!=1:
                        y.append(k+2)
            return y
                      
        else:
            # Creates a matrix where each row consists of (i^j)%n for j belongs to {2,...,n-1}.
            for i in range(2,n):
                for j in range(2,n):
                    x = pow(i,j,n)
                    t[i-2][j-2] = x
                
            b = []  
            y = []      
            for k in range(0,n-2):
                b = t[k]       
                # Check whether all elements in a row is unique or not.                       
                if len(np.unique(b))==n-2:               
                    y.append(k+2)
            return y  

    def babystepgiantstep(self):
        
        if discrete_log.is_prime(self.p)==True and self.k in discrete_log.prim(self.p):
            m = math.ceil(math.sqrt(self.p-1))
            x = pow(self.k,m,self.p)
            
            # Creates Giant step list
            Q = []
            for i in range(0,m): 
                q = pow(x,i,self.p)                        
                Q.append(q)
        
            R = []
            for i in range(1,self.p+1):
                if (i*self.k)%self.p==1:
                    z = i
                    break
            
            # Creates Baby step list
            for d in range(0,m):
                r = (self.n*(pow(z,d,self.p)))%self.p                         
                R.append(r)
            
            # For checking the values of q and r such that f(r) = h(q)
            for t in Q:          
                if t in R: 
                    return Q.index(t)*m + R.index(t)               
                
if __name__=='__main__':
    p = int(input('Enter prime: '))
    k = int(input('Enter base(primitive root of above given prime): '))
    n = int(input('Enter number: '))
    obj = discrete_log(p,k,n)
    print(obj.babystepgiantstep())
                                