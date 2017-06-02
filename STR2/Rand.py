import random
sproby=1
Vgadav=False
s=random.randint(1,100)
print('Ia zagadav chyslo. Sprobuy ugadaty ')
a=int(raw_input())

while (sproby<9) and (Vgadav==False) :
    sproby=sproby+1
    if a>s : print('Zabagato')
    if a<s : print('Zamalo')
    if a==s : Vgadav=True
    else: a=int(raw_input('Sprobuy shche raz, sproba %d\n'% sproby))


if Vgadav==True:
    print ('!!!!!Ty vgadav z %d sproby!!!!' % sproby)
else: print('??????? Idy v banu, ia zagadav chyslo %d ?????????' %s)
 