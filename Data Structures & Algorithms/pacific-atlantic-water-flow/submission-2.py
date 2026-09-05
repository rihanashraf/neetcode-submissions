class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        n, m =len(heights),len(heights[0])
        res = []

        def dfs(i, j, seen):
            seen.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r,c) not in seen and heights[r][c]>=heights[i][j]:
                    dfs(r,c, seen)

        
        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m-1, atl)

        for j in range(m):
            dfs(0, j, pac)
            dfs(n-1, j, atl)

        for i in range(n):
            for j in range(m):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i,j])
        return res        

        