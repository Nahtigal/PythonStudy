
applicant = raw_input("Enter the applicant's name: \n").upper()
#interviewer = raw_input("Enter the interviewer's name: \n")
#time = raw_input("Enter the appointment time: \n")

#print(interviewer, "will interview", applicant, "at", time)

i=len(applicant)-1
s=''
while i>=0:
    s=s+applicant[i]
    i=i-1
    print s
     
    