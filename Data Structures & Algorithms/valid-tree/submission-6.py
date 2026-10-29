class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #what is the condition for a valid tree
        from collections import defaultdict
        D = defaultdict(list)
        visit = set()

        for u, v in edges:
            D[u].append(v)
            D[v].append(u)

        def dfs(i, prev):
            visit.add(i)
            for nei in D[i]:
                if nei == prev:
                    continue
                if nei in visit and nei!=prev:
                    return False                
                if not dfs(nei, i):
                    return False
            return True         

        if not dfs(0, -1):
            return False

        return True if len(visit)==n else False


        

         
        