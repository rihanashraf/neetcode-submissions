class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        n, m = len(heights), len(heights[0])

        def dfs(r,c, visit, prev):
            if (r not in range(n) or c not in range(m) or (r,c) in visit or heights[r][c] <prev):
                return

            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])

        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m-1, atl, heights[i][m-1])
        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n-1, j, atl, heights[n-1][j])

        out = []

        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i, j) in atl:
                    out.append([i,j])

        return out

            

        
        
        