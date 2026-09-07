class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        D = defaultdict(list)
        seen = set()
        visit = set()

        def dfs(i, prev):
            if i in seen:
                return False
            if not D[i]:
                seen.add(i)
                return True
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


        if dfs(0, -1) == False:
            return False

        out = 0
        for i in seen:
            out+=1
        print(out)
        return True if out == n else False

         
        