class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0

        for number in seen:
            if number-1 not in seen:
                length = 0
                while number+length in seen:
                    length+=1
                maximum = max(maximum, length)

        return maximum

        

                    

        