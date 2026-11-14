class Solution:
    def rob(self, nums: List[int]) -> int:
        f={}
        n= len(nums)
        def search(i, su):

            if i >= n:
                return 0
            if i in f:
                return f[i]
            a= search(i+2, su)
            b= search(i+3, su)
            f[i]= max(a,b)+nums[i]
            return f[i]

        a= search(0, 0)
        b=search(1, 0)
        return max(a,b)