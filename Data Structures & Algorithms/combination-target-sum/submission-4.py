class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], [[],  0]

        def backtrack(i):
            if sol[1]== target:
                res.append(sol[0].copy())
                return

            if sol[1]>target or i==n:
                return

            sol[0].append(nums[i])
            sol[1]+=nums[i]
            backtrack(i)
            sol[0].pop()
            sol[1]-=nums[i]

            backtrack(i+1)

        backtrack(0)
        return res
        
    
