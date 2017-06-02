l=[]
while True:
    i=int(raw_input('Enter numbers< '))
    if i<0:
        break
    else:
        l.append(i)
avg=0.00

for i in l:
    avg=avg+i
    
avg=avg/(len(l))

for i in l:
    print 'Average of data %d'% i
print 'Is equal %f' % avg 
        
        