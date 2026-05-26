class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #O(1) space complexity to be used
        i = 0
        j = len(numbers)-1

        while i!=j:
            test = numbers[i] + numbers[j]
            if test < target:
                i+=1
            elif test>target:
                j-=1
            else:
                return [i+1, j+1]
        