class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def rob3(nums):
            rob1, rob2 = 0, 0 

            for n in nums:
                rob1, rob2 = rob2, max(rob2, rob1+n)
            return rob2

        if n==1:
            return nums[0]

        return max(rob3(nums[1:]), rob3(nums[:(n-1)]))


        