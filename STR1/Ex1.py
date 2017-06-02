import random
budget=1000000000
goverment=200000000
army=200000000
education=40000000
pensions=50000000
roads_and_fools=200000000 #hhhhhhhhhhhhhhhhhhhhhhhhh
nanotethnologies=300000000
expendes_total=goverment+army+education+pensions+roads_and_fools+nanotethnologies
balance=budget-expendes_total

print balance

ColodaCard=["Six","Six","Six","Six","Seven","Seven","Seven","Seven","Eight","Eight","Eight","Eight",\
"Nine","Nine","Nine","Nine","Ten","Ten","Ten","Ten","Valet","Valet","Valet","Valet",\
"Dame","Dame","Dame","Dame","KIng","KIng","KIng","KIng","Ace","Ace","Ace","Ace"]
Rozdacha=[]
random.shuffle(ColodaCard)
Rozdacha.append(ColodaCard.pop())
Rozdacha.append(ColodaCard.pop())
print Rozdacha
del Rozdacha
Rozdacha=[]
Rozdacha.append(ColodaCard.pop())
Rozdacha.append(ColodaCard.pop())
print Rozdacha

