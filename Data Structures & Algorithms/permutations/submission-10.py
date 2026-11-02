class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        seen = set()
        def dfs():
            if len(seen) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in seen:
                    sol.append(x)
                    seen.add(x)
                    dfs()
                    sol.pop()
                    seen.remove(x)


        dfs()
        return res

