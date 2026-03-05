lstStudent = []

iStudentId = int( input("Enter Your Student ID Number: "))
sFirstName = input("Enter Your First Name: ").upper()
sLastName = input("Enter your Last Name: ").upper()
fGPA = round(float(input("Enter your GPA: ")), 2)

lstStudent.append(iStudentId)
lstStudent.append(sFirstName)
lstStudent.append(sLastName)
lstStudent.append(fGPA)

#print(iStudentId, sFirstName, sLastName, fGPA)
iStudentId = int( input("Enter Your Student ID Number: "))
sFirstName = input("Enter Your First Name: ").upper()
sLastName = input("Enter your Last Name: ").upper()
fGPA = round(float(input("Enter your GPA: ")), 2)

lstStudent.append([iStudentId, sFirstName, sLastName, fGPA])

lstStudent.append(sFirstName)
lstStudent.append(sLastName)
lstStudent.append(fGPA)

lstStudent.append([iStudentId, sFirstName, sLastName, fGPA])

#print(iStudentId, sFirstName, sLastName, fGPA)
print(lstStudent [0])
print(lstStudent [1])


