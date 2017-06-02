way=float(raw_input("VVedit sliakh\n"))
time1=float(raw_input("Vvedit pershyy chas \n"))
speed1=float(raw_input("Vvedit pershu shvydkist \n"))
speed2= float(raw_input("Vedit drugu shvydkist \n"))

dist1=time1*speed1
dist2 = way-dist1 if(way-dist1)>0 else 0
#dist2=way-dist1

time2=dist2/speed2
time=time1+time2
print("Tourists ishly %.2f kilomiters, first %.2f godyn zi shvydkistu %.2f , a potim zi shvydkistu %.2f " % (way,time1,speed1,speed2))
print("Vidpovid: v dorozi tyrustu bylu %.2f godyn " % (time))