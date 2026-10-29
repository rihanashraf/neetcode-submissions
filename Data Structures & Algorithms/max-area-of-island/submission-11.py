class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        n, m = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if (i not in range(n) or j not in range(m) or (i, j) in seen or grid[i][j] == 0):
                return 0

            seen.add((i,j))
            return (1+dfs(i, j+1)+
                    dfs(i, j-1)+
                    dfs(i-1, j)+
                    dfs(i+1, j))


        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i, j))

        return maxarea


        

        
        