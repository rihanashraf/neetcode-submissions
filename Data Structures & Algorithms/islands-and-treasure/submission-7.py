class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])
        q = collections.deque()

        def addRoom(r,c):
            if (r not in range(n) or c not in range(m) or grid[r][c] !=INF):
                return
            grid[r][c] = add+1
            q.append((r,c))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))

        add = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                addRoom(r,c+1)
                addRoom(r, c-1)
                addRoom(r+1, c)
                addRoom(r-1, c)
                
            add+=1


