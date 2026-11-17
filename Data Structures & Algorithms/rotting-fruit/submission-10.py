class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we need to rot the fruits till all of them are rotten, else return -1

        q = collections.deque()
        n, m = len(grid), len(grid[0])

        seen = set()
        mins = 0
        f = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    f+=1
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen.add((i,j))
        if f==0:
            return 0

        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while q and f>0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in dirs:
                    r, c = i+dr, j+dc
                    if r in range(n) and c in range(m) and (r,c) not in seen and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2
                        seen.add((r,c))  
                        f-=1          

            mins+=1


        return mins if f ==0 else -1

        
                    
        