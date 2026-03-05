# Create a dictionary where the keys are snack names and the values are the quantities of those snacks.
# You can use whatever snacks and numbers you want.
# (e.g., "chips": 3, "cookies": 5, "granola bars": 2, etc.).

dictSnack = {
    "Fruit Snack": 1,
    "Apple Sauce": 2,
    "Oreos": 20
}


# Print Current snack inventory:
print("Current snack inventory:")
# Then print out your dictionary. It's fine that it appears with the curly braces:
print(dictSnack)


# Add a new snack:

# Prompt the user to add a new snack:
sNewSnack = input("Enter the name of a new snack to add: ")

# If the snack is already in the dictionary, print:
# <new snack> is already in your inventory.
if sNewSnack in dictSnack:
    print(sNewSnack, "is already in your inventory.")
else:
    # If the snack is not in the dictionary, prompt the user to enter the quantity:
    iSnackCount = int(input("Enter the count for " + sNewSnack + ": "))
    # Then add the new snack name and quantity to the dictionary
    dictSnack[sNewSnack] = iSnackCount
    # and print:
    # <new snack> was added to your inventory.
    print(sNewSnack, "was added to your inventory.")


# Update the count for an existing snack**:

# Prompt the user to enter the name of a snack they want to update:
sUpdateSnack = input("Enter the name of a snack to update: ")

# If the snack is in the dictionary, prompt the user to enter the new count:
if sUpdateSnack in dictSnack:
    iNewCount = int(input("Enter the new count for " + sUpdateSnack + ": "))
    # Then update the count for the snack
    dictSnack[sUpdateSnack] = iNewCount
    # and print:
    # The count for <snack> was updated.
    print("The count for", sUpdateSnack, "was updated.")
else:
    # If the snack is not in the dictionary, print:
    # <snack> is not in your inventory.
    print(sUpdateSnack, "is not in your inventory.")


# Remove a snack by name:

# Prompt the user to enter the name of a snack they want to remove:
sRemoveSnack = input("Enter the name of a snack to remove: ")

# If the snack is in the dictionary, remove it and print:
if sRemoveSnack in dictSnack:
    dictSnack.pop(sRemoveSnack)
    print(sRemoveSnack, "was removed from your inventory.")
else:
    # If the snack is not in the dictionary, print:
    print(sRemoveSnack, "is not in your inventory.")


# Print the final snack inventory:

print("Final snack inventory:")
# Then print out your dictionary with all updates applied.
print(dictSnack)
