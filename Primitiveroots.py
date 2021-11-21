# Calculation of Primitive roots for a number
import numpy as np
import math

# Greatest common divisor of two numbers

class primitive:
    
    def __init__(self,N):
        self.N = N
    
    def gcd(a,b):
        if a == 0 or b==0:
            if a + b == 0:
                return 'GCD does not exist'
            else:
                return a + b
        else:
            return primitive.gcd(b%a,a)
    
    #Euler Totient function    
    def euler_phi(n):  
        count = 0
        for i in range(1,n+1):
            if primitive.gcd(i,n)==1:
                count = count + 1
        return count
    
    # Function check for prime numbers    
    def prime_check(n):
        if n<=1:
            return 'Invalid input'
        for i in range(2,int(math.sqrt(n))+1):
            if primitive.gcd(n,i)==1:
                continue
            else:
                return(str(n)+' is not a prime number.')
                break
        return str(n)+' is a prime number.' 
    
    # Computation of primitive roots
    def prim(self):
        n = abs(self.N)
        t = np.zeros((n-2,n-2))
        if primitive.prime_check(n) == 'Invalid input':
            return 'Primitive roots does not exist'
            
        
        elif primitive.prime_check(n)==str(n)+' is not a prime number.':
            # Creates a matrix where each row consists of (i^j)%n for j belongs to {2,...,n-1}.
            for i in range(2,n):
                for j in range(2,n):
                    x = pow(i,j,n)
                    t[i-2][j-2] = x
                    
            b = []  
            y = []      
            for k in range(0,n-2):
                b = t[k]                       # Check whether cardinality of unique elements in a row is unique or not.
                if len(np.unique(b))==primitive.euler_phi(n): 
                    if primitive.gcd(k+1,n)!=1:
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
                b = t[k]                              # Check whether all elements in a row is unique or not.
                if len(np.unique(b))==n-2:               
                    y.append(k+2)
            print(str(self.N),'has',str(len(y)),'primitive roots as given below.')
            return y
        
if __name__=='__main__':
    x = int(input('Enter no : '))
    obj = primitive(x)
    print(obj.prim())
