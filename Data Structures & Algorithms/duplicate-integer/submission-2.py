class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = set()


        for i in range(len(nums)):
            if nums[i] in empty:
                return True
            empty.add(nums[i])

        return False
            
            
    
        