class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #what is the beginning of a sequence? it is the number which doestn have a (n-1) value in the hashmap
        seen = set(nums)
        maximum = 0
        for number in seen:
            length = 1
            if number-1 not in seen:
                while number+1 in seen:
                    length+=1
                    number +=1
            maximum = max(maximum, length)

        return maximum
            


                    

        