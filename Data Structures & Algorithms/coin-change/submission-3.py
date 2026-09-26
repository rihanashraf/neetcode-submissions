class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("INF")]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for n in coins:
                if (i-n)>=0:
                    dp[i] = min(dp[i], 1+dp[i-n])
                
        return dp[amount] if dp[amount]!= float("INF") else -1

                

        


        