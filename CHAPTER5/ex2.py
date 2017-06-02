s=int(raw_input("enter number: "))
if s>0 and s<=100 :
    Quaters,s = divmod(s,25)[:2]
    Dime,s = divmod(s,10)[:2]
    Nickel,Cents=divmod(s,5)[:2]
    print "You can got %d Quaters, %d Dimes, %d Nikels and %d Cents" % (Quaters,Dime,Nickel,Cents)
else:
    print "Enter number between 0 and 100"
    