class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #looks like multi source bfs
        INF = 2147483647
        n,m = len(grid), len(grid[0])

        q = collections.deque()
        seen = set()

        def add(i, j):
            if (i>=n or i<0 or j>=m or j<0 or (i,j) in seen or grid[i][j] == -1):
                return 
            q.append((i,j))
            seen.add((i,j))



        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))
        s = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if grid[i][j] == INF:
                    grid[i][j] = s
                add(i+1, j)
                add(i-1, j)
                add(i, j+1)
                add(i, j-1)
            s+=1
        





        

        


