# Jordan Harris
# Prompt For Song Name
sSongName = input("Enter the name of a song: ")

# Prompt For Song Rating Between 0 and 10
iSongRating = int(input("On a scale of 0 to 10, 10 being the highest, how much do you like the song? "))
#Prompt for the band
sBand = int( input("Enter the name of the band or artist:"))

# Determine if they liked the song
if (irating >= 7) or (sBand.upper() == "Queen") : 
    print("You really like the song!")
    print("Let's Go Listen To It Now!")
elif (iSongRating >= 5) :
    print('you sorta like that song. ')
elif (iSongRating >= 2) :
    print("What a trash song. ")
else : 
    print("Yah that song sucks! ")
    print("Find another song")

print("Goodbye! ")