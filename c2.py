#Jordan Harris
#The program collects win and loss data for multiple teams and calculates the average win percentage.
# Create a list to store all teams
lstTeams = []

# Ask how many teams
iNumberOfTeams = int(input("Enter the # of Teams: "))

# Loop to enter each team
for iCount in range(0, iNumberOfTeams):

    print("Entering data for team", iCount + 1)

    sName = input("Enter The Name of the Team: ")
    iWins = int(input("Enter The # of Wins: "))
    iLosses = int(input("Enter The Number of Losses: "))

    # Store team data in a dictionary
    dictTeam = {
        "Name": sName,
        "Wins": iWins,
        "Losses": iLosses
    }

    # Add dictionary to list
    lstTeams.append(dictTeam)


# Calculate average win percentage
fTotalWinPct = 0

print("\nTeams Records:")
for dictTeam in lstTeams:
    iTotalGames = dictTeam["Wins"] + dictTeam["Losses"]
    fWinPct = dictTeam["Wins"] / iTotalGames
    fTotalWinPct = fTotalWinPct + fWinPct

    print(dictTeam["Name"], "Win %:", fWinPct)

fAverageWinPct = fTotalWinPct / iNumberOfTeams

print("\nAverage Win Percentage:", fAverageWinPct)
