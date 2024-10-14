class BuyAndSell:
    def __init__(self, lst):
        self.lst = lst

    def find_profit(self):
        profit = 0
        for i in range(1, len(self.lst)):
            # Only add to profit when the price increases
            if self.lst[i] > self.lst[i-1]:
                profit += self.lst[i] - self.lst[i-1]
        return profit

# Example usage
lst = [1,2,3,4,5]
is_profit = BuyAndSell(lst)

print(is_profit.find_profit()) 

