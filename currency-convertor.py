# Take the first input – the currency that you have. It is default for all the calculations.
# Retrieve the data from FloatRates as before.
# Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance).
# Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have.
# Check the cache. Maybe you already have what you need?
# If you have the currency in your cache, calculate the result.
# If not, get it from the site, and calculate the result.
# Save the rate to your cache.
# Print the result.
# Repeat steps 4-9 until there is no currency left to process.

import requests

# initialize cache
cache = {}

# initailize variables 
your_currency = None
currency_code = None
money = None

def input_validator():
    global your_currency, currency_code, money
    # this will be a flag variable
    input_valid = False

    while not input_valid:
        your_currency_valid = False
        currency_code_valid = False
        money_valid = False

        while not your_currency_valid:
            your_currency = input('What is the currency code that you want to exchange?: ').lower()
            if your_currency == 'exit':
                return # exit out of this function if 'exit' is entered
            if len(your_currency) == 3:
                your_currency_valid = True
            else:
                print(f'Your currency must be a 3 digit code. You put in a {len(your_currency)} digit code!')
        
        
        while not currency_code_valid:
            currency_code = input('What is the currency code that you want to convert to?: ').lower()
            if currency_code == 'exit':
                return # exit out of this function if 'exit' is entered
            if len(currency_code) == 3:
                currency_code_valid = True
            else:
                print(f'Your currency must be a 3 digit code. You put in a {len(currency_code)} digit code!')
            
        while not money_valid:
            try:
                money = float(input('Please input the amount of money you have: '))
                if money == 'exit':
                    return # exit out of this function if 'exit' is entered
                elif money > 0:
                    money_valid = True
                else: 
                    print("You must enter a valid number greater than zero for the amount of money you have.")
            except (ValueError):
                print('You must put in a valid number for the amount of money you have.')
        
        if your_currency_valid and currency_code_valid and money_valid: 
            input_valid = True

def main():
    while True:
        input_validator()
        if any(variable == 'exit' for variable in (your_currency, currency_code, money)):
            break # Exit the main loop if 'exit' is entered
        print("Checking the cache...")

        if currency_code not in cache:
            url = f'http://www.floatrates.com/daily/{your_currency}.json'
            response = requests.get(url)
            rates = response.json()
            # print(data['usd'])
            print("Sorry, but it is not in the cache!")
            # put the rate in the cache
            cache[currency_code] = rates[currency_code]
        elif currency_code in cache:
            print("Oh! It is in the cache!")
        
        # calculate the exchanged currency by multiplying your money and the exchange rate of the currency you want
        your_exchange = cache[currency_code]['rate'] * money
        # print the rate from the cache
        print(f'You receieved {your_exchange} {currency_code.upper()}.')
        print(cache)

main()
