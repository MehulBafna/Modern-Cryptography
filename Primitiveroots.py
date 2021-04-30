# Calculation of Primitive roots of a prime number n
import numpy 
import math

# Greatest common divisor of two numbers
def gcd(a,b):
    if a == 0 or b==0:
        if a + b == 0:
            return 'GCD does not exist'
        else:
            return a + b
    else:
        return gcd(b%a,a)

# Function check for prime numbers    
def prime_check(n):
    if n<=1:
        return 'Invalid input'
    for i in range(2,int(math.sqrt(n))+1):
        if gcd(n,i)==1:
            continue
        else:
            return(str(n)+' is not a prime number.')
            break
    return str(n)+' is a prime number.' 

# Computation of primitive roots
def prim(n):
    if n==0:                         
        return 'No primitive roots exist'         # Since for zero we have no primitive roots.
    
    
    if prime_check(abs(n))==str(n)+' is not a prime number.':
      return 'Enter Valid prime number' 
      
    elif n>0:
        t = numpy.zeros((n,n))                # Creates a matrix where each row consists of (i^j)%n for j belongs to {1,...,n-1}.
        for i in range(0,n):
            for j in range(0,n):
                x = pow(i,j,n)
                t[i][j] = x
            
        b = []  
        y = []      
        for k in range(0,n-1):
            b = t[k]                              # Check whether all elements in a row is unique or not.
            #print numpy.unique(b),b
            if len(numpy.unique(b))==n-1:               
                y.append(k)
        return y  
             
    else:
        return prim(-n)  
