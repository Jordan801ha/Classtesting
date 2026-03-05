#Jordan Harris
#create a funciton
#promot user to choose menuitem
#add value to a list
#delete removes the last element in the list
#display Shows all elements of the ist
#exit gets out of the loop
#return the choice they selected

def showMenue() :
    while (True) :
        print("1. Add")
        print("2. Delete")
        print("3. Display")
        print("4. Exit/n")

        iChoice = int(input("Make a selection"))

        if (iChoice != 1 and iChoice != 2 and iChoice != 3 and iChoice != 4) :
            print("Enter a valid choice!")

        else :
            return iChoice
        
iChoice = 0 

while (iChoice != 4) :
    iChoice = showMenue()

    if (iChoice ==1) :
        #do the add dictionary ot a list
    elif (iChoice == 2) :
    elif (iChoice == 3) :
    elif (ichoice == 4) :
        print("have a nice day!")
