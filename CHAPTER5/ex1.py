def D_Sum(a,b):
    return a+b
def PrintSum(s=0):
        print "The sum is %d" % int(s)

if __name__ == "__main__":
    s=raw_input("Enter two number separate by comas")
    t=()
    t=s.split(',')
    PrintSum(D_Sum(int(t[0]),int(t[1])))
    
        

    