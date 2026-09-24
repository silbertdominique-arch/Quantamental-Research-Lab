def calculate_return(starting_price, ending_price):
    return (ending_price - starting_price) / starting_price


prices = [100, 103, 101, 106]
daily_returns = []

for i in range(1, len(prices)):
    previous_price = prices[i - 1]
    current_price = prices[i]
    daily_return = calculate_return(previous_price, current_price)
    daily_returns.append(daily_return)
    print(f"${previous_price} to ${current_price}: {daily_return * 100:.2f}%")


average_daily_return = sum(daily_returns) / len(daily_returns)

growth_factor = 1

for daily_return in daily_returns:
    growth_factor = growth_factor * (1 + daily_return)

cumulative_return = growth_factor - 1

print(f"Cumulative return: {cumulative_return * 100:.2f}%")

print(f"Average daily return: {average_daily_return * 100:.2f}%")