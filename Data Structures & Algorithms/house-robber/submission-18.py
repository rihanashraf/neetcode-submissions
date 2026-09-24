class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = {0:nums[0], 1:max(nums[1], nums[0])}
        
        def f(x):
            if x in dp:
                return dp[x]
            dp[x] = max(f(x-1), nums[x]+f(x-2))
            return dp[x]

        return f(n-1)
            