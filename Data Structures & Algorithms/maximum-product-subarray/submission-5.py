class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maximum = nums[0]
        minimum = nums[0]

        for i in range(1, len(nums)):
            store = maximum
            maximum = max(nums[i], nums[i]*maximum, nums[i]*minimum)
            minimum = min(nums[i], nums[i]*minimum, nums[i]*store)

            res = max(res, maximum)
            
        return res




            
        
        