class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        D = defaultdict(list)
        seen = set()

        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)
            for nei in D[i]:
                if nei == prev:
                    continue
                if dfs(nei, i) == False:
                    return False
            return True

        for i, j in edges:
            D[i].append(j)
            D[j].append(i)


        return dfs(0,-1) and len(seen) ==n

         
        