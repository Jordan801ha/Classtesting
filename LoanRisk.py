#Jordan Harris
#inputs
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
fIncome = float(input("Enter your annual income in dollars: "))
fDebt = float(input("Enter your total monthly debt payments in dollars: "))

#Calculate the DTI (Debt-to-Income Ratio) using the following formula:
#The DTI should be rounded to the 2nd decimal place.
fDTI = fDebt / (fIncome / 12)
fDTI = round(fDTI, 2)


#Classify the DTI according to the following categories:

if fDTI < 0.20:
    sCategory = "Low Risk"
elif fDTI < 0.36:
    sCategory = "Moderate Risk"
elif fDTI < 0.50:
    sCategory = "Elevated Risk"
else:
    sCategory = "High Risk"
#Print out the user's first name, last name, DTI, and DTI category in the following format:
print(sFirstName, sLastName, fDTI, sCategory)
#<first name> <last name> has a DTI of <dti>. The associated category is: <category>.""
