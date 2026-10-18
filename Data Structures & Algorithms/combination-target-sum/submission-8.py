class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol= [], [[], 0]
        n = len(nums)

        def dfs(i):
            if sol[1]==target:
                res.append(sol[0][:])
                return

            if sol[1]>target or i ==n:
                return 
            
            sol[0].append(nums[i])
            sol[1]+=nums[i]
            dfs(i)
            sol[1]-=nums[i]
            sol[0].pop()

            dfs(i+1)


        dfs(0)
        return res
    
