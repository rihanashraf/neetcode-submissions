class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(i, total, cur):
            if total==target:
                res.append(cur[:])
                return

            if total>target or i==n:
                return

            cur.append(candidates[i])
            backtrack(i+1, total+candidates[i], cur)
            cur.pop()

            while i+1<n and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, total, cur)

        backtrack(0, 0, [])
        return res