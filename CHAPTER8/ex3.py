s=raw_input('enter string for analisys: ')

vovels=('a','o','e','i','u')
d={}
count=0
for i in s:
    if i in vovels:
        count+=1    

print 'There are %d vovels in string'%count        
        
    