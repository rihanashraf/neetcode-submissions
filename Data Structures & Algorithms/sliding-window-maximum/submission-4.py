class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        dicti = {}
        l, r = 0, k-1

        maximum = float("-inf")

        for i in range(k):
            dicti[nums[i]] = 1+dicti.get(nums[i], 0)
            maximum = max(maximum, nums[i]) 
        output.append(maximum)

        while r <len(nums)-1:
            maximum = float("-inf")
            dicti[nums[l]] -=1
            l+=1
            r+=1
            dicti[nums[r]] = 1+dicti.get(nums[r], 0)

            for char in dicti:
                if dicti[char]>0:
                    maximum = max(maximum, char)

            output.append(maximum)

        return output

            
        




        