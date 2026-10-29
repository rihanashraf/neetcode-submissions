class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #some kind of bfs problem

        fresh = 0
        rotten = 0
        mins = 0
        q = collections.deque()
        n, m = len(grid), len(grid[0])

        def add(r, c):
            nonlocal fresh
            if (r not in range(n) or c not in range(m) or grid[r][c]!=1):
                return 
            grid[r][c] = 2
            fresh-=1
            q.append((r,c))

        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                add(r+1, c)
                add(r-1, c)
                add(r, c+1)
                add(r, c-1)
            mins+=1                  

        return mins if fresh==0 else -1

        
                    
        