from collections import Counter
from itertools import product
import random
from tabulate import tabulate
from fractions import Fraction as frac

class byzantine_agreement:
    
    def __init__(self,n):
        self.n=n

    def byzantine_agreement_r1(self):
        m = random.randint(0,int((self.n-1)/3))
        if self.n>=3*m+1:
            # List of permutations of length 2 for pairwise           exchange of information.
            x = list(product(list(range(1,self.n+1)),repeat=2)) 
            # List denoting private information of each user.
            y = [0]*len(list(range(self.n))) 
            for i in range(len(y)):
                w = random.randint(1,self.n+1)
                if w not in y:
                    y[i]=random.randint(1,self.n+1)
            # List for storing private information of user i            corresponding to pairwise permutation.   
            z = [0]*len(x) 
            # Malicious or faulty users list
            M = []
            for i in range(m):
                if random.choice(list(range(1,self.n+1))) not in M:
                    M.append(random.choice(list(range(1,self.n+1)))) 
            # Sharing of information on one-by-one basis.   
            for i in range(len(z)):
                for j in range(0,self.n):
                    if x[i][0]==j+1:
                        z[i]=y[j]
                    if x[i][0] in M:
                        z[i]=random.randint(1,self.n)
            # List storing each information shared.
            R1 = []
            R1.append(['User i','User j','User i -> User j '])
            for i in x:
                for j in range(0,len(z)):
                    if x.index(i)==j:
                        R1.append([i[0],i[1],z[j]])
                        
            for i in range(1,len(R1),self.n+1):
                R1[i][2]='Same user.'
            
            print(' Communicating information ')
            print()
            print(tabulate(R1,headers='firstrow',tablefmt="pretty"))
            return R1,M
        else:
            return 'Byzantine agreement prerequisite not satisfied.'
    
    @staticmethod
    def byzantine_agreement_r2(L,n):
        
        if L =='Initial byzantine agreement prerequisite not satisfied.':
            return L
        else:
            print()
            print(' Shared information analysis ')
            print()
            # Creating vector of information obtained from each user 
            # j by each user i and i!=j
            M = []
            M.append(['User i','Value of other user(s) denoted as [j,v] where user j has value v (as per user i)'])
            for j in range(1,n+1):
                N = []
                for i in L[0]:
                    if L[0].index(i)>0:
                        if i[1]==j and i[0]!=i[1]:
                            N.append([i[0],i[2]])
                M.append([j,N])
            
            print(tabulate(M,headers='firstrow',tablefmt="pretty"))
            P=[]
            
            for i in M:
                if M.index(i)>0:
                    for j in i[1]:
                        P.append(tuple(j))
        
            # Concluding final correct value obtained by majority 
            # and thus rendering malicious users.
            R2 = []
            R2.append(('User','Agreed value','Fraction of users agreed with value'))
            Y = []
            W = []
            for k,v in Counter(P).items():
                if n==4:
                    if v/(n-1) >=2/3:
                        R2.append((k[0],k[1],frac(v-len(L[1]),(n-1))))
                        W.append(k[0])
                    else:
                        if k[0] not in Y:
                            Y.append(k[0])
                        
                elif n>4:
                    if v/(n-1) >2/3:
                        R2.append((k[0],k[1],frac(v-len(L[1]),(n-1))))
                        W.append(k[0])
                    else:
                        if k[0] not in Y:
                            Y.append(k[0])             
        print()
        Z = []
        for i in Y:
            if i not in W:
                Z.append('User '+str(i)+' is malicious.')
                R2.append((i,'NIL',1-frac(len(L[1])-v,(n-1))))
        
        print(tabulate(R2, headers='firstrow',tablefmt="pretty"))
        print()  
        if len(Z)!=0:
            return Z
        else:
            return 'All users are honest.'

if __name__=='__main__':
    n = int(input('Enter number of users: '))
    print()
    if 0<n<3:
        print(str(n)+' are honest.') 
    elif n<=0:
        print('Enter valid quantity.')
    else:
        obj = byzantine_agreement(n)
        x = obj.byzantine_agreement_r1()
        print(byzantine_agreement.byzantine_agreement_r2(x,n))