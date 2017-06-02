def D (p=()):
    return p[1]*p[1]-4*p[0]*p[2]>0
    
F=lambda a,b,c: b*b-4*a*c

seq=((1,2,3),(1,6,1),(2,10,2),(2,8,10))    

ops=(lambda a:a*a,lambda a:a*a*a,lambda a:a*a*a*a)

#p=(1,2,3) 

#ops={'F': F}

#print apply(ops['F'],seq[0])

    
z=[op(6) for op in ops]

print z

qq=lambda a,b:a*b
o=(45,89)
print apply(qq,(45,78))