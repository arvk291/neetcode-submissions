class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_val, max_profit = prices[0], 0
        for val in prices[1:]:
            if lowest_val > val:
                lowest_val = val
            else:
                profit = val - lowest_val
                if profit > max_profit:
                    max_profit = profit
        return max_profit