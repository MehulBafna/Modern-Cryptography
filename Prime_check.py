import math


def gcd(a,b):
    if a == 0 or b==0:
        if a + b == 0:
            return 'GCD does not exist'
        else:
            return a + b
    else:
        return gcd(b%a,a)
    
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
