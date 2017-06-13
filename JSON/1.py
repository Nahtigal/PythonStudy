import json

fileName = 'user_setting.txt'
myFile = open(fileName,mode='w')

Player1 ={
    'Name':'Ramon',
    'Score':456,
    'Items':['Wild hog','Magic wand','Some shit']
    
}

Player2 ={
    'Name':'Patrik',
    'Score':478,
    'Items':['Magic ring','Iron but','Double bubble']
    
}

AllTogether = []
AllTogether.append(Player1)
AllTogether.append(Player2)

#------------------Save by JSON-------------
json.dump(AllTogether,myFile)
myFile.close()
