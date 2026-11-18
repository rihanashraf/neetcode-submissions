class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return [] if you find a cycle
        D = defaultdict(list)
        seen = set()
        visit = set()
        out = []

        def dfs(i):
            if i in seen:
                return False
            if i in visit:
                return True
            seen.add(i)
            for nei in D[i]:
                if not dfs(nei):
                    return False

            seen.remove(i)
            if i not in visit:
                out.append(i)
            visit.add(i)
            return True


        for u, v in prerequisites:
            D[u].append(v)

        for i in range(numCourses):
            if not dfs(i):
                return []
            if len(out) == numCourses:
                return out


        

        


        

        
        
        

        
        
        