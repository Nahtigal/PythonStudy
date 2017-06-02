try:
    ff=float('10,25')
    f=open('ex21.py')
    for x in f.readlines():
        print x
except (ValueError,TypeError), d:
    print "error ocuer"
    print str(d)
except IOError, E:
    print str(E)
#except ValueError:
 #   print 'Float convert error'

    