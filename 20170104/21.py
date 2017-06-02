import random

in_file = open('money.txt')
Money = int(in_file.read())
in_file.close()

MyScore=0
Comp_Score=0
Win=False
def Cards_Score(argument):
    switcher = {
        "Six"  : 6,
        "Seven": 7,
        "Eight": 8,
        "Nine" : 9,
        "Ten"  : 10,
        "Valet": 2,
        "Dame" : 3,
        "KIng" : 4
    }
    return switcher.get(argument,0)

def Scr (Card,Who):
    Score=0
    for x in Card:
        if x=='Ace' :
            point =  11 if Score+11<=21 else 1
            Score = Score + point
        else:    
            Score= Score + Cards_Score(x)  
        
    print(Who + ' card is: ' + ', '.join(str(x) for x in Card))
    print Who + ' score is %d' % Score 
    return Score

# Promt for stavka    
print('You got %d grivnas.Lets play' % Money)
ColodaCard=["Six","Six","Six","Six","Seven","Seven","Seven","Seven","Eight","Eight","Eight","Eight",\
"Nine","Nine","Nine","Nine","Ten","Ten","Ten","Ten","Valet","Valet","Valet","Valet",\
"Dame","Dame","Dame","Dame","KIng","KIng","KIng","KIng","Ace","Ace","Ace","Ace"]
if Money<=0:
    print "No money no game"
    quit()
Stavka=int(raw_input('Iaka vasha stavka\n'))
if Stavka>Money:
    print "You have no sach money. We willplay for %d grivnas" %Money
    Stavka=Money

Rozdacha=[]
random.shuffle(ColodaCard)
Rozdacha.append(ColodaCard.pop())
Rozdacha.append(ColodaCard.pop())

MyScore=Scr(Rozdacha,'Your')

ans=raw_input('Do you want anothe one Y/N \n')
while ans.upper()=='Y':
    Rozdacha.append(ColodaCard.pop())
    MyScore=Scr(Rozdacha,'Your')
    if MyScore>=21: break
    ans=raw_input('Do you want anothe one Y/N \n')
    
print ('Your final score is %d' % MyScore)

if MyScore>21 :
    print ("You got more then 21. You lost")
elif  MyScore==21 :
    print ("You got 21. You WIN !!!!!!")
    Win=True
else:
    del Rozdacha
    Rozdacha=[]
    random.shuffle(ColodaCard)
    Rozdacha.append(ColodaCard.pop())
    Rozdacha.append(ColodaCard.pop())
    Comp_Score=Scr(Rozdacha,'Comp')
    while Comp_Score<=MyScore and Comp_Score!=21:
       Rozdacha.append(ColodaCard.pop())
       Comp_Score=Scr(Rozdacha,'Comp')

    if Comp_Score>21 :
       print ("Comp got more then 21. You win")
       Win=True
    elif Comp_Score>=MyScore :
        print "Comp got more or equal. You lost"
    else: 
        print "You got more then comp. You win"
        Win=True
if Win :
    Money=Money+Stavka*1.2
else :
    Money=Money-Stavka
print "Now your money is %d" % Money

out_file = open('money.txt', 'w')
out_file.write(str(Money))
out_file.close