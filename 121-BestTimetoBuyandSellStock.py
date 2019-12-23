# This solution does not pass due to time complexity. This runs with O(n**2) which times out one the website due to the nested for loops.
# I have included a reworked solution below that stays within the time contraints. 

# Nested for loop solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_max = 0
        for index, buy_day in enumerate(prices):
            for i in range(index + 1, len(prices)):
                # Making the buying day negative to show spending money
                profit = (-1 * buy_day) + prices[i]
                if profit > running_max:
                    running_max = profit
        
        if running_max <= 0:
            return 0
        return running_max

# Single iteration solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_lowest = float('inf')
        running_max = 0
        for price in prices:
            if price < running_lowest:
                running_lowest = price
            elif price - running_lowest > running_max:
                running_max = price - running_lowest
        return running_max