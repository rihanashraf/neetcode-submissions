class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for i in range(len(nums)):
            dicti[nums[i]] = i

        for i in range(len(nums)):
            num = target - nums[i]
            if num in dicti and dicti[num]!=i:
                return [i, dicti[num]]

                    