class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #you need to make a graph structure and then see if it has a cycle or not

        D = defaultdict(list)
        visit = set()
        seen = set()

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
            visit.add(i)
            return True


        for u, v in prerequisites:
            D[u].append(v)

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        
        
        