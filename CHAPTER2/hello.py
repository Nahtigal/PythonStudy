import MyModule

i = float(raw_input('now enter number < '))
if i<0 :
    print '%d is less then zero'%i
elif i>0 :
    print '%d is greate then zero'%i
else: 
    print 'zero is zero'


print MyModule.SomeTestFunction()

tt=10
print 'The function result is %d'% MyModule.ParametrF(tt)
print 'And now original value of tt %d' % tt
