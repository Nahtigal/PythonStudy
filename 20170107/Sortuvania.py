
def bubleSort (spysok):
    i=0
    j=len(spysok)
    zmina=False
    while j>1:
        for i in range(j-1):
            if spysok[i]>spysok[i+1]:
                spysok[i],spysok[i+1]=spysok[i+1],spysok[i]
                zmina=True
        print spysok
        if zmina==False: 
            break
        else : zmina=False
        j=j-1
        
def bubleSortReliz1(spysok):
    i=1
    for i in range(len(spysok)-1):
        j=len(spysok)-1
        while j>i:
            if spysok[j]<spysok[i]:
                spysok[j],spysok[i]=spysok[i],spysok[j]
            j=j-1    
        print spysok


s=raw_input("Enter numbers for sorting separated by commas\n")
spysok=[int(n) for n in s.split(',')]

bubleSort(spysok)
print "Another aprouch\n"

bubleSortReliz1(spysok)
