from sys import argv



script,arg1,arg2,arg3,arg4 = argv


way=float(arg1)
time1=float(arg2)
speed1=float(arg3)
speed2= float(arg4)

dist1=time1*speed1
dist2 = way-dist1 if(way-dist1)>0 else 0
#dist2=way-dist1

time2=dist2/speed2
time=time1+time2
print("Tourists ishly %.2f kilomiters, first %.2f godyn zi shvydkistu %.2f , a potim zi shvydkistu %.2f " % (way,time1,speed1,speed2))
print("Vidpovid: v dorozi tyrustu bylu %.2f godyn " % (time))