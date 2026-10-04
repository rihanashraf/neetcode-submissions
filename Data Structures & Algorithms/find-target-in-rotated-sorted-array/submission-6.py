class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r= 0, len(nums)-1

        while l<=r:
            m = l+(r-l)//2
            if nums[m]==target:
                return m

            #left sorted
            elif nums[l]<=nums[m]:
                if target>nums[m]:
                    l=m+1
                elif target>=nums[l]:
                    r=m-1
                else:
                    l=m+1
            
            #right sorted
            else:
                if target<nums[m]:
                    r = m-1
                elif target<=nums[r]:
                    l=m+1
                else:
                    r=m-1

        return -1