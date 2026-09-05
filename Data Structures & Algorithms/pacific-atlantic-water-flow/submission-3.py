class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        n, m =len(heights),len(heights[0])
        res = []

        def dfs(i, j, seen, prev):
            if i<0 or i==n or j<0 or j==m or (i, j) in seen or heights[i][j] < prev:
                return 
            seen.add((i, j))
            dfs(i+1, j, seen, heights[i][j])
            dfs(i-1, j, seen, heights[i][j])
            dfs(i, j+1, seen, heights[i][j])
            dfs(i, j-1, seen, heights[i][j])
            
        
        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m-1, atl, heights[i][m-1])

        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n-1, j, atl, heights[n-1][j])

        for i in range(n):
            for j in range(m):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i,j])
        return res        

        