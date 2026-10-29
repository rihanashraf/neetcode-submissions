class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        n, m = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            seen.add((i,j))
            area = 1
            dirs = [[0, 1], [0, -1], [1, 0], [-1,0]]

            for dr, dc in dirs:
                r,c = i+dr, j+dc
                if (r in range(n) and c in range(m) and (r,c) not in seen and grid[r][c] == 1):
                    area +=dfs(r,c) 

            return area  
            

        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i, j))

        return maxarea


        

        
        