class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        n = len(grid)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, r, c= heapq.heappop(minH)
            if (r, c) in visit:
                continue
            
            visit.add((r,c))

            if r == n-1 and c == n-1:
                return t

            for dr, dc in directions:
                i, j = r+dr, c+dc
                if i not in range(n) or j not in range(n) or (i,j) in visit:
                    continue

                heapq.heappush(minH, [max(t, grid[i][j]), i, j])



            

        
                


        