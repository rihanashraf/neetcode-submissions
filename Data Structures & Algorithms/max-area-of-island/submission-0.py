class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        n = len(grid)
        m = len(grid[0])
        seen = set()
        def dfs(i, j):
            seen.add((i, j))
            area = 1
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                r, c = i+dr, j +dc
                if 0<=r<n  and 0<=c<m and (r,c) not in seen and grid[r][c]==1:
                    seen.add((r, c))
                    area += dfs(r, c)
            return area
                       
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i,j))

        return maxarea



        