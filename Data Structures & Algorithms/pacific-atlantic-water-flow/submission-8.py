class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from the corners and have separate traversals for pacific and atlantic??
        pac = set()
        atl = set()
        n,m = len(heights), len(heights[0])

        def dfs(i,j,h,s):
            if (i not in range(n)) or (j not in range(m)) or (i,j) in s or heights[i][j]<h:
                return
            s.add((i,j))

            dfs(i,j-1, heights[i][j], s)
            dfs(i,j+1, heights[i][j], s)
            dfs(i+1,j, heights[i][j], s)
            dfs(i-1,j, heights[i][j], s)


        for i in range(n):
            for j in range(m):
                if (i==0 or j==0):
                    dfs(i,j, -1, pac)

                if (i==n-1 or j==m-1):
                    dfs(i,j, -1, atl)

        out = []

        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in atl:
                    out.append([i,j])

        return out

                

        

        
            

        
        
        