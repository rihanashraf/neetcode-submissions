class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a valid tree is essentially a connected acyclic graph
        #if you start dfs on one of the edges you need to be able to reach all of them essentially - in order to know if there is a cycle - you'll need to keep track of what the prev was essentially. if its in the seen set and its not prev, then its a cycle??
        D = defaultdict(list)
        seen = set()

        def dfs(i, prev):
            seen.add(i)
            for nei in D[i]:
                if nei in seen and nei!=prev:
                    return False
                elif nei in seen:
                    continue
                if not dfs(nei, i):
                    return False
            return True



        for u,v in edges:
            D[u].append(v)
            D[v].append(u)



        if not dfs(0, -1):
            return False
        print(seen)
        for i in range(1, n):
            if i not in seen:
                return False

        return True

        


        

        

        

        

        

         
        