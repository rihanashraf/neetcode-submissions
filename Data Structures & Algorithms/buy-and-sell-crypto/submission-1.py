class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_value = prices[0]
        max_profit = 0
        profit = 0
        for i in range(len(prices)):
            curr = prices[i]
            if curr >min_value:
                profit = curr - min_value
            else:
                min_value = curr
            if profit >max_profit:
                max_profit = profit
        return max_profit


        