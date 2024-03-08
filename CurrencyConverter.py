from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Input the amount to convert
amount = int(input("Enter amount you want to convert:\n"))

# Input the currency to convert from
from_currency = input("From currency (e.g., USD, EUR, GBP):\n").upper()

# Input the currency to convert to
to_currency = input("To currency (e.g., USD, EUR, GBP):\n").upper()

# Convert the currency
result = c.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")



# Note ::: Some Currencies are not available so Enjoy and feel free to contact me " :) "