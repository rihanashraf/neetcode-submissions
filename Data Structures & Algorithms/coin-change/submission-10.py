class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top-down how to solve this???
        #base case is reaching the amount and then backtrack if overshoot as well
        dp = {amount:0}
        def dfs(x):
            if x>amount:
                return float("INF")
            if x in dp:
                return dp[x]

            ans = float("INF")

            for c in coins:
                ans = min(ans,1+dfs(x+c))
            dp[x] = ans
            return dp[x]
                       

        return dfs(0) if dfs(0) != float("INF") else -1





        


                

        


        