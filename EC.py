#Jordan Harris
# This code will take a string, reverse it and print it out

sName = input("Enter Your Name: ")

sReversed = ""  

# loop through the string backward
for i in range(len(sName) - 1, -1, -1):
    sReversed = sReversed + sName[i]

print(sReversed)