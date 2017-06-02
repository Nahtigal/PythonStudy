'looks for substring counts FindIn what, where'
import string
import sys

def checkArgs():
    if len(sys.argv) != 3:
        
        print 'Need two arguments what and where'
        sys.exit(1)
    else:
        
        print 'Argumets1  %s  Argument2 %s '% (sys.argv[1],sys.argv[2])
        print LookFor(sys.argv[1],sys.argv[2])
        
def LookFor(what,where):
    count=0
    start=string.find(where,what,0)
    while start>-1:
        count+=1
        start=string.find(where,what,start+1)
    return count
    
if __name__=='__main__':
    
    checkArgs()
    
    
    