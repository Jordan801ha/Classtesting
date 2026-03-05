#Function 2:adds together 2 numbers and returns the result.
def sum_two_numbers (a, b) :
    return (a + b) 

#Function 3: Tells you wheather an integer is even or odd

def is_even(num):
    return num % 2 == 0

#function 4: 
def get_number_parity(num):
    if is_even(num):
        return f"{num} is even."
    else:
        return f"{num} is odd."
    
#Function 5
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

#Function 6
def min_max_mean(numbers_list):
    lowest = min(numbers_list)
    highest = max(numbers_list)
    mean = sum(numbers_list) / len(numbers_list)
    return [lowest, highest, mean]

#Function 7
def dog_message(name, age=0):
    return f"I am a dog named {name} and I'm {age} years old!"

#Function 8
def classify_age(age, senior_age=65):
    if age < 18:
        return "Minor"
    elif age < senior_age:
        return "Adult"
    else:
        return "Senior"
    
#Function 9
def calculate_total(price, quantity, discount_percent, threshold_total=100, bonus_discount=0.02):
    
    total = price * quantity
    
    if total > threshold_total:
        discount_percent = discount_percent + bonus_discount
    
    discounted_total = total * (1 - discount_percent)
    
    return round(discounted_total, 2)