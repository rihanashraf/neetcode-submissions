class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {0:cost[0], 1:cost[1]}

        def dfs(i):
            if i in dp:
                return dp[i]

            dp[i] = min(dfs(i-1)+cost[i], dfs(i-2)+cost[i])
            return dp[i]

        return min(dfs(n-1), dfs(n-2))
        
         
            
