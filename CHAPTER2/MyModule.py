
"This is the test module \
and nothing more about it"

import sys

def SomeTestFunction():
    return 'Pyton '+ sys.version[:6]+ ' on '+ sys.platform
    
def PrintVersion():
    print 'Pyton '+ sys.version[:6]+ ' on '+ sys.platform    

def ParametrF (a=0):
    a+=5
    return a
if __name__ == '__main__':
    PrintVersion()
else:
    print __name__
    
    
    

