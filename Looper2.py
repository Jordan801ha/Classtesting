#create a list to store sudents
lstStudent = []

#Prompt for the number of students
iNumStud= int(input(How many students? ")
                    
#loop to gather Data
for iCount in ragnge(0, iNumStud) : 
    #Gather id (int), first Name, last name
    iId = int(input("What is the dtudent id: ")
    sFirst = input("Enter the first name ")
    sLast = input("Enter The Last Name")

#Store lists
    lstStudent.append([iId, sFirst, sLast])

print(lstStudent)