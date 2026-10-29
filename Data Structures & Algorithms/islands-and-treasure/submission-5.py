class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()

        def addRoom(r,c):
            if (r not in range(n) or c not in range(m) or (r,c) in seen or grid[r][c] ==-1):
                return

            seen.add((r,c))
            q.append((r,c))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))

        add = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = add
                addRoom(r,c+1)
                addRoom(r, c-1)
                addRoom(r+1, c)
                addRoom(r-1, c)
                
            add+=1


