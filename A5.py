# Jordan Harris
# This code will randomly generate scores for each game the selected team will play
# and display information on the Home teams performance.

import random

# Enter Name and Game information
sName = input("Enter the name of your home team: ")
iGames = int(input("Enter the number of games that " + sName + " will play: "))

print()

iWins = 0
iLosses = 0
dictResults = {
    "Won Against": [],
    "Lost Against": []
}

for iGameNum in range(1, iGames + 1):

    sAwayTeam = input("Enter the name of the away team for game " + str(iGameNum) + ": ")

    # Generate scores 0 to 3, but no ties allowed
    iHomeScore = random.randint(0, 3)
    iAwayScore = random.randint(0, 3)

    while iHomeScore == iAwayScore:
        iHomeScore = random.randint(0, 3)
        iAwayScore = random.randint(0, 3)

    # Print the scores in the required format
    print(sName + "'s score: " + str(iHomeScore) + " - " + sAwayTeam + "'s score: " + str(iAwayScore))
    print()

    # Determine win or loss and store away team name
    if iHomeScore > iAwayScore:
        iWins = iWins + 1
        dictResults["Won Against"].append(sAwayTeam)
    else:
        iLosses = iLosses + 1
        dictResults["Lost Against"].append(sAwayTeam)


#print results
print("Teams won against:")
for team in dictResults["Won Against"]:
    print(" ", team)

print()
print("Teams lost against:")
for team in dictResults["Lost Against"]:
    print(" ", team)

print()
print("Final season record:", iWins, "-", iLosses)

# Final message  
fWinPct = iWins / iGames

if fWinPct >= 0.75:
    print("Qualified for the NCAA Soccer Tournament!")
elif fWinPct >= 0.50:
    print("You had a good season.")
else:
    print("Your team sucks, go practice!")