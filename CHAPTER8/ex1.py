import random
Rez=(random.randint(1,100),random.randint(1,100),random.randint(1,100))

Trys=1
Valid=0

while Trys<=3:
    print 'in the loop'
    Ans=int(raw_input('%d Try.Enter number.'%Trys))
    Trys+=1
    for i in Rez:
        if Ans==i:
            Valid=1    
            break
    if Valid:
        print 'You guess number %d in list' % Ans
        print Rez
        break
    
    
        
if Valid==0: 
    print 'You havent guess. The answer was'
    print Rez