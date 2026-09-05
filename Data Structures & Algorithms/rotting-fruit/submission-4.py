class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        seen = set()
        if not grid:
            return -1

        n,m = len(grid), len(grid[0])
        from collections import deque
        q = deque()
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    fresh +=1

        while q and fresh!=0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[0, 1], [0, -1],[1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if 0<=row<n and 0<=col<m and grid[row][col] == 1 and (row, col) not in seen:
                        grid[row][col] = 2
                        q.append((row, col))
                        seen.add((row, col))
                        fresh -=1
            time+=1
        


    
        return time if fresh == 0 else -1
        
        