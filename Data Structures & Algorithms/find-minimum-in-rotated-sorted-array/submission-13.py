class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float("inf")

        while l<=r:
            m = (l+r)//2
            minimum = min(minimum, nums[m])

            #left partition
            if nums[l]<=nums[m]:
                if nums[l]>nums[r]:
                    l = m+1
                else:
                    r = m-1

            #right partition
            else:
                r = m-1



        return minimum

            



        
        