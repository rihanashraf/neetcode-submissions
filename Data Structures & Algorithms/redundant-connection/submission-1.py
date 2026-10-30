class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #detect cycle and need to see which edge corresponds to the cycle essentially

        D = defaultdict(list)

        def dfs(u,v):
            if u ==v:
                return True
            visit.add(u)
            
            for nei in D[u]:
                if nei not in visit:
                    if dfs(nei,v):
                        return True
            return False
        for u,v in edges:
            visit = set()
            if dfs(u,v):
                return [u,v]
            D[u].append(v)
            D[v].append(u)

                        

        
        