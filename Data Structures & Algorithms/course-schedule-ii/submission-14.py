class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #we need to find order 
        from collections import defaultdict
        D = defaultdict(list)
        seen = set()
        visit = set()

        def dfs(i):
            if i in visit:
                return False
            if i in seen:
                return True
            visit.add(i)

            for nei in D[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            seen.add(i)
            out.append(i)
            return True

        for u,v in prerequisites:
            D[u].append(v)

        out = []
        for i in range(numCourses):
            if i not in seen:
                if not dfs(i):
                    return []

        return out
        

        
        
        