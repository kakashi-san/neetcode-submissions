class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0] 
        max_profit = 0

        for price in prices:
            min_ = min(price, min_)
            profit = price - min_
            max_profit = max(max_profit, profit)

        return max_profit