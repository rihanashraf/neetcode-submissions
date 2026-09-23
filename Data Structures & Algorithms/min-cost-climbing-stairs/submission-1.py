class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {0:0, 1:0}

        def f(x):
            if x in dp:
                return (dp[x]+cost[x])
            if x == 0 or x==1:
                return (dp[x]+cost[x])
            dp[x] = min(f(x-1), f(x-2))

            return (dp[x]+cost[x])

        return min(f(n-1), f(n-2))
            
