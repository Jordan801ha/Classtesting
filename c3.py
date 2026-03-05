#Jordan Harris
#impo
import random

def win_loss_gen (numGames) : 
    iWins = random.randrange(0, numGames +1)

#Caluclate the leftover number gmaes to looser
    iLosses = numGame - iWins

 return iWins, iLosses 
# Create a list to store all teams
lstTeams = []

# Ask how many teams
iNumberOfTeams = int(input("Enter the # of Teams: "))

#ask how many games are played
iGames = int(input("Enter The Number Of Games Played"))

# Loop to enter each team
for iCount in range(0, iNumberOfTeams):

    print("Entering data for team", iCount + 1)

    sName = input("Enter The Name of the Team: ")
    iWins = int(input("Enter The # of Wins: "))
    iLosses = int(input("Enter The Number of Losses: "))

#calculate the random number between 0 and the number of wins
    #call the function to get wins and losses
    wins, losses = win_loss_gen (iGame)

    # Store team data in a dictionary
    Teams.append= ({
        "Name": sName,
        "Wins": iWins,
        "Losses": iLosses
    })

    # Add dictionary to list
    lstTeams.append()


# Calculate average win percentage
iWins = 0
iLosses = 0

print("\nTeams Records:")
for dictTeam in lstTeams:
    iTotalGames = dictTeam["Wins"] + dictTeam["Losses"]
    fWinPct = dictTeam["Wins"] / iTotalGames
    fTotalWinPct = fTotalWinPct + fWinPct


fAverageWinPct = fTotalWinPct / iNumberOfTeams

print
