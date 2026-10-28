class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])  
        seen = set()
        islands = 0

        def bfs(i, j):
            seen.add((i,j))
            q = collections.deque()
            q.append((i,j))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(n) and c in range(m) and (r,c) not in seen and grid[r][c] == "1"):
                        q.append((r,c))
                        seen.add((r,c)) 
                    
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == "1":
                    islands+=1
                    bfs(i, j) 

        return islands      