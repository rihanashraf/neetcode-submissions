class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #any start of a sequence is when that
        seen = set(nums)
        maximum = 0
        for number in nums:
            if number-1 not in seen:
                length = 1
                while number+1 in seen:
                    length+=1
                    number = number+1
                maximum = max(maximum, length)

        return maximum

        




                    

        