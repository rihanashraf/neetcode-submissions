class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        for number in nums:
            if number not in dicti:
                dicti[number] = 1
            else:
                return True
        return False
        