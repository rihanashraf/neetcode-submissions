class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]
        maxim = nums[n-1]

        for i in range(n-3, -1, -1):
            dp[i] = nums[i] + maxim
            maxim = max(dp[i+1], dp[i+2])
            print(maxim)

        return max(dp)

            