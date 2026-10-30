class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        profit = 0
        while high < len(prices):
            profit = max(profit, prices[high] - prices[low]) 
            if(prices[high] < prices[low]):
                low = high
            high += 1
        return profit
