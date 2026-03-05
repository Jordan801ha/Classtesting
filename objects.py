#Jordan Harris Section 004
# This program allows the user to enter multiple students and the courses
# each student is enrolled in. The program stores the information using
# Student and Course classes and then displays the results.

class Course:
    def __init__(self, number, name):
        self.number = number
        self.name = name


class Student:
    def __init__(self):
        self.netid = ""
        self.first_name = ""
        self.last_name = ""
        self.courses = []   # list of Course objects


lstStudents = []

# Get student count safely
bContinue = True
while bContinue:
    try:
        iStudCnt = int(input("How many students? "))
        bContinue = False
    except ValueError:
        print("Enter a number.")

# Collect students + their courses
for i in range(iStudCnt):
    oStud = Student()
    oStud.netid = input("Enter NetID: ")
    oStud.first_name = input("Enter first name: ")
    oStud.last_name = input("Enter last name: ")

    # Get course count safely
    while True:
        try:
            iCourseCnt = int(input("How many courses? "))
            break
        except ValueError:
            print("Enter a number.")

    for j in range(iCourseCnt):
        sNum = input("Enter the course number: ")
        sName = input("Enter the course name: ")
        oCourse = Course(sNum, sName)
        oStud.courses.append(oCourse)

    lstStudents.append(oStud)

# Print results
print("\nStudents Entered:")
for oStud in lstStudents:
    print(oStud.netid, oStud.first_name, oStud.last_name)
    for oCourse in oStud.courses:
        print(oCourse.number, oCourse.name)