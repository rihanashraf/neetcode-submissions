class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        islands = 0

        def dfs(i, j):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r = i+dr
                c = j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen and grid[r][c] == "1":
                    seen.add((r, c))
                    dfs(r, c)

        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == "1":
                    islands+=1
                    dfs(i, j)


        return islands        