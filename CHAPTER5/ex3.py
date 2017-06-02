def Fact(n):
    Ans={}
    d=2
    while d*d <= n:    
        if n%d==0:
            if d in Ans:
                Ans[d]+=1
            else:
                Ans[d]=1
            n /= d
        else:
            d+=1
    if n > 1:
        if n in Ans:
            Ans[n]+=1
        else:
            Ans[n]=1
    return Ans    
    
    
    
a=int(raw_input('Enter first number: '))    
b=int(raw_input('Enter second number: '))    



FactA=Fact(a)
FactB=Fact(b)
print FactA
print FactB

#Take max for existing keys
for x in FactA.keys():
    FactA[x] = max(FactA.get(x,0),FactB.get(x,0))
    
#Adding values for not existing keys
for x in FactB.keys():    
    if x not in FactA:
        FactA[x]=FactB.get(x,0)
        
print FactA        
s=1
for x in FactA.keys():
    s=s*x**FactA[x]
    
print s

    









    
        


    
    

    
        
