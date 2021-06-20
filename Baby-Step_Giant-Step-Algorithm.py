#Computation of discrete logarithm using baby-step-giant-step-algorithm

import math
import numpy as np

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
def gcd(a,b):
    if a == 0 or b==0:
        if a + b == 0:
            return 'GCD does not exist'
        else:
            return a + b
    else:
        return gcd(b%a,a)

#Euler Totient function    
def euler_phi(n):  
    count = 0
    for i in range(1,n+1):
        if gcd(i,n)==1:
            count = count + 1
    return count

# Computation of primitive roots
def prim(N):
    n = abs(N)
    t = np.zeros((n-2,n-2))
    if is_prime(n)==False:
        return 'Primitive roots does not exist'
        
    elif is_prime(n)==False:
        # Creates a matrix where each row consists of (i^j)%n for j belongs to {2,...,n-1}.
        for i in range(2,n):
            for j in range(2,n):
                x = pow(i,j,n)
                t[i-2][j-2] = x        
        b = []  
        y = []      
        for k in range(0,n-2):
            b = t[k]                       # Check whether cardinality of unique elements in a row is unique or not.
            if len(np.unique(b))==euler_phi(n): 
                if gcd(k+1,n)!=1:
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
        return y  

def babystepgiantstep(p,k,n):
    
    if is_prime(p)==True and k in prim(p):
        m = math.ceil(math.sqrt(p-1))
        x = pow(k,m,p)
    
        Q = []
        for i in range(0,m): 
            q = pow(x,i,p)                        # Creates Giant step list
            Q.append(q)
    
        R = []
        for i in range(1,p+1):
            if (i*k)%p==1:
                z = i
                break
                
        for d in range(0,m):
            r = (n*(pow(z,d,p)))%p                         # Creates Baby step list
            R.append(r)
        
        for t in Q:          
            if t in R: 
                return Q.index(t)*m + R.index(t)               # For checking the values of q and r such that f(r) = h(q)
                            
