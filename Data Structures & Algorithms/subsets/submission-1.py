class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def bactrack(i):
            if i==n:
                res.append(sol[:])
                return
            bactrack(i+1)
            
            sol.append(nums[i])
            bactrack(i+1)
            sol.pop()
        


        bactrack(0)
        return res