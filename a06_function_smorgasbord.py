#Jordan Harris
#A6- this program will write out 9 seperate functions and call each of them.

import a06_my_functions 

# Function 1: welcome_message (Prints out a message w/ a person's name)
def welcome_message(sName) :
    print("Hello " + sName + ", Welcome to IS 303")

welcome_message("Diego")
welcome_message("Mai")

#Function 2:
print(a06_my_functions. sum_two_numbers(5, 7))
print(a06_my_functions. sum_two_numbers(1000.5, -30))

#Function 3:
print(a06_my_functions.is_even(7))
print(a06_my_functions.is_even(120))

#Function 4: 
print(a06_my_functions.get_number_parity(5))
print(a06_my_functions.get_number_parity(10)) 

#function 5: 
print(a06_my_functions. fahrenheit_to_celsius(32))
print(a06_my_functions.fahrenheit_to_celsius(75))

#funciton 6: 
numbers_list_1 = [20, 45, 23, 2, 87, 3]
print(a06_my_functions.min_max_mean(numbers_list_1))

#Function 7
print(a06_my_functions.dog_message("Spot", 7))
print(a06_my_functions.dog_message("Peppy"))

#Function 8
print(a06_my_functions.classify_age(60, 55))
print(a06_my_functions.classify_age(62))

#Function 9
for i in range(2):
    
    price = float(input("Enter the price for the product purchased: "))
    quantity = int(input("Enter the quantity of the product purchased: "))
    discount_percent = float(input("Enter the discount percent (formatted as a decimal): "))
    
    total = a06_my_functions.calculate_total(price, quantity, discount_percent)
    
    print(f"The total price after discounts is: ${total}")