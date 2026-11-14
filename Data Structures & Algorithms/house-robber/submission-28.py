class Solution:
    def rob(self, nums: List[int]) -> int:
        f={}
        n= len(nums)
        def search(i):

            if i >= n:
                return 0
            if i in f:
                return f[i]
            a= search(i+2)
            b= search(i+3)
            f[i]= max(a,b)+nums[i]
            return f[i]

        a= search(0)
        b=search(1)
        return max(a,b)