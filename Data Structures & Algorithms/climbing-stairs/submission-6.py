class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:1, 1:1}
        def f(x):
            if x in dp:
                return dp[x]
            dp[x] = f(x-1)+f(x-2)
            return dp[x]
        return f(n)