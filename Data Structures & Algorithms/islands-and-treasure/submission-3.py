class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        from collections import deque
        q = deque()
        seen = set()

        def addRoom(i, j):
            if i < 0 or i==n or j<0 or j ==m or (i, j) in seen or grid[i][j] == -1:
                return 
            q.append((i, j))
            seen.add((i, j))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = length
                addRoom(r+1, c)
                addRoom(r, c+1)
                addRoom(r-1, c)
                addRoom(r, c-1)
            length +=1

