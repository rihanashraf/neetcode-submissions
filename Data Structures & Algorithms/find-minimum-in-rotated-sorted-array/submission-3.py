class Solution:
    def findMin(self, nums: List[int]) -> int:
        #what is the O(n) solution

        minimum = float("INF")

        for i in range(len(nums)):
            minimum = min(minimum, nums[i])

        return minimum