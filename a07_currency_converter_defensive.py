#Jordan Harris
# This program converts US dollars to another currency.

conversion_rates = {
    "EUR": 0.93,  # Euro
    "GBP": 0.81,  # British Pound
    "JPY": 133.0, # Japanese Yen
    "INR": 82.5,  # Indian Rupee
    "AUD": 1.48,  # Australian Dollar
    "CAD": 1.36,  # Canadian Dollar
    "CHF": 0.92,  # Swiss Franc
    "CNY": 7.15,  # Chinese Yuan
    "SEK": 10.5,  # Swedish Krona
    "NZD": 1.62,  # New Zealand Dollar
    "MXN": 18.0,  # Mexican Peso
}

while True:
    dollar_input = input("Enter an amount in US dollars: ").strip()

    # check if it's a valid positive decimal number like 30 or 30.5
    check_number = dollar_input.replace(".", "", 1)
    if not check_number.isdecimal():
        print(f"{dollar_input} is not a valid number. Please try again.")
        continue

    dollars = float(dollar_input)

    print("Foreign currencies available for conversion are:")
    for code in conversion_rates:
        print(code, end=" ")
    print()

    currency_input = input("Please enter a target currency (e.g., EUR, GBP): ")
    currency = currency_input.strip().upper()

    if currency not in conversion_rates:
        print(f"{currency} is not a valid currency. Please try again.")
        continue

    rate = conversion_rates[currency]
    foreign_amount = dollars * rate

    print(f"{dollars:.2f} USD is equal to {foreign_amount:.2f} {currency}")
    break