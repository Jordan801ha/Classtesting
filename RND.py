# Jordan Harris
# This program collects test information for two students
# and displays their average test scores.


# Prompt for student 1 full name
sFullName1 = input("Enter student 1 full name: ")

# Prompt for student 1 birth year
iBirthYear1 = int(input("Enter student 1 birth year: "))

# Prompt for number of tests
iNumTests1 = int(input("Enter number of tests: "))

# Prompt for sum of test scores
fSumScores1 = float(input("Enter the sum of test scores: "))

# Calculate average and round to 2 decimals
fAvgTest1 = round(fSumScores1 / iNumTests1, 2)

# Display results
print(sFullName1.upper(), "born in", iBirthYear1, "scored", fSumScores1,
      "points on", iNumTests1, "tests for an average of", fAvgTest1, "%")

print()  # blank line between students



# Prompt for student 2 full name
sFullName2 = input("Enter student 2 full name: ")

# Prompt for student 2 birth year
iBirthYear2 = int(input("Enter student 2 birth year: "))

# Prompt for number of tests
iNumTests2 = int(input("Enter number of tests: "))

# Prompt for sum of test scores
fSumScores2 = float(input("Enter the sum of test scores: "))

# Calculate average and round to 2 decimals
fAvgTest2 = round(fSumScores2 / iNumTests2, 2)

# Display results
print(sFullName2.upper(), "born in", iBirthYear2, "scored", fSumScores2,
      "points on", iNumTests2, "tests for an average of", fAvgTest2, "%")