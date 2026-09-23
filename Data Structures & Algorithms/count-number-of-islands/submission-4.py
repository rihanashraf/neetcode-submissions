class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        isls = 0
        n, m = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            seen.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen and grid[r][c] == "1":
                    seen.add((r, c))
                    dfs(r, c)
            

        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == "1":
                    isls+=1
                    dfs(i, j)

        return isls

        