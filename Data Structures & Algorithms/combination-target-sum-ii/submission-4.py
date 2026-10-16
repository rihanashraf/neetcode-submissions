class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            if i == n or total>target:
                return

            cur.append(candidates[i])
            backtrack(i+1, total+candidates[i], cur)
            cur.pop()

            j=i+1
            while j<n and candidates[i]== candidates[j]:
                j+=1
            backtrack(j, total, cur)



        backtrack(0, 0, [])
        return res
