input_days = [7,9,6,4,3,1]

max_profit = 0      # Initialize maximum profit
buy_day = 0         # Day to buy
sell_day = 0        # Day to sell

# Iterate through all combinations of buy and sell
for i in range(len(input_days)):
    for j in range(i + 1, len(input_days)):
        buy_price = input_days[i]
        sell_price = input_days[j]
        
        # Calculate profit
        profit = sell_price - buy_price
        
        # Check if this profit is the best we have found
        if profit > max_profit:
            max_profit = profit
            buy_day = i          # Day to buy (index)
            sell_day = j         # Day to sell (index)

# Output results
if max_profit > 0:
    print(f"Maximum Profit: {max_profit}")
    print(f"Buy on Day: {buy_day + 1} (Price: {input_days[buy_day]})")
    print(f"Sell on Day: {sell_day + 1} (Price: {input_days[sell_day]})")
else:
    print("No profit possible.")
