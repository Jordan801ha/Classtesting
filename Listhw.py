#Jordan Harris
lstGroceries = ["Cheese", "Rice", "Chicken"]

# Print the current grocery list
print(lstGroceries)

# Add a new item to the list

# Prompt the user to add a new grocery item
sNewItem = input("Enter a new grocery item to add: ")

# Add the item to the end of the list
lstGroceries.append(sNewItem)

# Check for a specific item
# Prompt the user to enter an item to check
sCheckItem = input("Enter an item to see if it's in your list: ")

# Check if the item is in the list
if sCheckItem in lstGroceries:
    print(sCheckItem, "is in your list.")
else:
    print(sCheckItem, "is not in your list.")


# Remove an item by name
# Prompt the user to enter an item to remove
sRemoveItem = input("Enter an item to remove from the list: ")

# Check if the item exists before removing
if sRemoveItem in lstGroceries:
    lstGroceries.remove(sRemoveItem)
    print(sRemoveItem, "was removed from the list.")
else:
    print(sRemoveItem, "is not in your list.")

# Remove the first item from the list
sFirstItem = lstGroceries.pop(0)

# Print which item was removed
print("The first item,", sFirstItem, ", was removed from the list.")

# Print the final list

print("Final grocery list:")
print(lstGroceries)
