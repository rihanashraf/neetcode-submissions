class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])

        maximum = 0

        for number in seen:
            if number-1 not in seen:
                j=1
                length = 1
                while number+j in seen:
                    length+=1
                    j+=1
                maximum = max(maximum, length)

        return maximum

        

                    

        