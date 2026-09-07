class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        D = defaultdict(list)
        seen = set()

        def dfs(i):
            seen.add(i)
            for nei in D[i]:
                if nei not in seen:
                    dfs(nei)
            return
                
        for i, j in edges:
            D[i].append(j)
            D[j].append(i)
        

        out = 0
        for i in range(n):
            if i not in seen:
                out+=1
                dfs(i)
        return out
        