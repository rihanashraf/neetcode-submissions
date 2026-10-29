class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #some kind of bfs problem

        fresh = 0
        mins = 0
        q = collections.deque()
        n, m = len(grid), len(grid[0])

        def add(r, c):
            if (r not in range(n) or c not in range(m) or grid[r][c]!=1):
                return False
            grid[r][c] = 2
            q.append((r,c))
            return True

        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                fresh -=add(r+1, c)
                fresh -=add(r-1, c)
                fresh -=add(r, c+1)
                fresh -=add(r, c-1)
            mins+=1                  

        return mins if fresh==0 else -1

        
                    
        