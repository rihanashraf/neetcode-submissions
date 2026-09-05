class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        res = []
        

        def pacific(i, j, seen):
            seen.add((i, j))
            if i ==0 or j ==0:
                return True
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r,c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen and heights[r][c]<=heights[i][j]:
                    seen.add((r, c))
                    if pacific(r, c, seen):
                        return True
            return False 
            
        def atlantic(i, j, seen):
            seen.add((i, j))
            if i ==n-1 or j ==m-1:
                return True
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r,c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen and heights[r][c]<=heights[i][j]:
                    seen.add((r, c))
                    if atlantic(r, c, seen):
                        return True
            return False 


        for i in range(n):
            for j in range(m):
                if pacific(i, j, set()) and atlantic(i,j, set()):
                    res.append([i, j])
        return res

        