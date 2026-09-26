class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}

        for i in range(len(nums)):
            dicti[nums[i]]= i



        for i in range(len(nums)):
            search = target - nums[i]
            if search in nums and dicti[search]!=i:
                return [i,dicti[search]]

        

        