one=1
two=1
step=1
n=10


print one
print two
while step<=n:
    one,two=two,one+two
    print 'step %d number is %d'% (step,two)
    step+=1