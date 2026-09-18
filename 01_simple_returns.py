def calculate_return(starting_price, ending_price):
    return (ending_price - starting_price) / starting_price

starting_price = float(input("Enter the starting price: "))
ending_price = float(input("Enter the ending price: "))

if starting_price <= 0:
    print("Error: Starting price must be greater than zero")
elif ending_price < 0:
    print("Error: Ending price must be greater than zero")

else:
    dollar_change = ending_price - starting_price

    decimal_returns = calculate_return(starting_price, ending_price)
    percent_returns = decimal_returns * 100

    print(f"Dollar change: ${dollar_change:.2f}")
    print(f"Decimal return: {decimal_returns:.4f}")
    print(f"Percentage return: {percent_returns:.2f}%")

