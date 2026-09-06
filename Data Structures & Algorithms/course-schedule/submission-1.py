class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        D = defaultdict(list)   
        seen = set()

        def dfs(node):
            if not D[node]:
                return True
            if node in seen:
                return False
            seen.add(node)
            for nei in D[node]:
                if not dfs(nei):
                    return False
            seen.remove(node)
            D[node]= []
            return True





        for i, j in prerequisites:
            D[i].append(j)

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
        
        