class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        n = len(candidates)
        candidates.sort()


        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return
            elif total>target or i == n:
                return

            cur.append(candidates[i])
            dfs(i+1, total+candidates[i])
            cur.pop()

            while i+1<n  and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)

        dfs(0, 0)
        return res       