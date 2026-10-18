class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, total, cur):
            if total==target:
                res.append(cur.copy())
                return

            if total>target or i==n:
                return

            cur.append(nums[i])
            dfs(i, total+nums[i], cur)
            cur.pop()

            dfs(i+1, total, cur)


        dfs(0, 0, [])
        return res
    
