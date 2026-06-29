class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        mini = float("INF")
        while l <=r:
            m = l+(r-l)//2

            minimum = min(nums[l], nums[r], nums[m])
            if minimum <mini:
                mini = minimum
            if nums[m]> nums[l]:
                l = m+1
            elif nums[m] < nums[l]:
                r = m-1
            else:
                return mini
        
        