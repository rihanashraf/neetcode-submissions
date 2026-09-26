class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top-down how to solve this???
        #base case is reaching the amount and then backtrack if overshoot as well
        #how to think of recursive solutions is the main problem

        INF = float("INF")
        dp = [-1]*(amount+1)
        dp[0]= 0
        

        def dfs(x):
            if dp[x]!=-1:
                return dp[x]
            dp[x] = INF

            for c in coins:
                if (x-c)>=0:
                    dp[x] = min(dp[x], 1+dfs(x-c))

            return dp[x]

        ans = dfs(amount)
        return ans if ans!=INF else -1




        


                

        


        