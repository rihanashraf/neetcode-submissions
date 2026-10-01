class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #how would we go about this, what is the base case of this recursive problem. when we reach the end of the string
        #how to write the lis dfs solution with cache
        dp = {len(nums)-1 : 1}

        def lis(i):
            if i in dp:
                return dp[i]

            dp[i] = 1

            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    dp[i] = max(dp[i], 1+lis(j))
            return dp[i]

        for i in range(len(nums)):
            lis(i)
        return max(dp.values())

            


        