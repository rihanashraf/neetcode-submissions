class Solution:
    def findMin(self, nums: List[int]) -> int:
        #what is the O(logn) solution
        #need to do binary search, take advantage of the fact that it is sorted in some way

        l, r = 0, len(nums)-1

        while l<=r:
            m = l+(r-l)//2
            if nums[m] <nums[r]:
                r = m
            else:
                l = m+1

        return nums[m]
                        



        