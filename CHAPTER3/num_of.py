t=tuple(raw_input('Enter a string for analisys:'))
d={}
for x in t:
        if x in d:
            d[x]+=1
        else:
            d[x]=1

for x in sorted (d):
   print ('Leter %r meets %d times') % (x,d[x]) 
            
                
    