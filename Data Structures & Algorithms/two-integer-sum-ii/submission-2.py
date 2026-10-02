class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #O(1) additional space
        #no hashmaps or anything like that
        n = len(numbers)
        i, j = 0,n-1 
        

        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1

        
            

        

                  