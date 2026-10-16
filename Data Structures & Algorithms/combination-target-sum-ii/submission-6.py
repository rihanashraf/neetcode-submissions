class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(pos, cur, target):
            if target == 0:
                res.append(cur[:])
                return
            if target<=0:
                return

            prev = -1
            for i in range(pos, n):
                if prev == candidates[i]:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, target-candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res        