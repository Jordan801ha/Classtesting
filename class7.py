#create a list to store sudents
lstStudent = []

#Prompt for the number of students
iNumStud= int(input(How many students? "))
                    
#loop to gather Data
for iCount in ragnge(0, iNumStud) : 
    #Gather id (int), first Name, last name
    iId = int(input("What is the dtudent id: ")
    sFirst = input("Enter the first name ")
    sLast = input("Enter The Last Name")

    #Store lists
    lstStudent.append({"id" : iId, "first" : sFirst, "Last" : sLast})

#display a menu
#1 - add, 2 delete, 3 - Display, 4 - Exit
#as long as they dont press 4, and choose 1, 2 or 3, then do something
while True : 
    print("Choose an option ")
    Print("1 - add ")
    Print("2 - Delter ")
    Print("3 - Display ")
    print("4 - Exit ")

    iChoice = int(input("Make your selection: ")
                  
    if (ichoice == 1) :
    
        iId = int(input("What is the dtudent id: ")
        sFirst = input("Enter the first name ")
        sLast = input("Enter The Last Name")
    
        #Store lists
        lstStudent.append({"id" : iId, "first" : sFirst, "Last" : sLast})
 
    elif (iChoice == 2) : 
    iStud = int(input("Which student id to delte: ")
    for student in lstStudents : 
        ifiStuend["id"] == iStud : 
            lstStudents.remove(student) 
            break 
    elif (iChoice ==3) : 
        print(lstStudents)

     elif (iChoice ==4) :
        break
    
    
print(lstStudent)
