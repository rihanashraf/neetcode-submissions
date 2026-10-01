class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #how would we go about this, what is the base case of this recursive problem. when we reach the end of the string
        dp = [1]*(len(nums))
        dp[len(nums)-1] = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)


        