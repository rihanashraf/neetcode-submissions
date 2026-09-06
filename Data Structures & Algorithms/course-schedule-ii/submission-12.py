class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        D = defaultdict(list)
        seen = set()
        visit = set()
        res = []

        def dfs(i):
            if i in seen:
                return False
            if i in visit:
                return True
            seen.add(i)
            for nei in D[i]:
                if dfs(nei) == False:
                    return False
            visit.add(i)
            res.append(i)
            seen.remove(i)
            return True
                        
        for i, j in prerequisites:
            D[i].append(j)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return res



        
        
        