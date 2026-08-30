class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0 
        n, m = len(grid), len(grid[0])
        q = collections.deque()


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append([i, j])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh >0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if 0<=r<n and 0<=c<m and grid[r][c] == 1:
                        q.append([r, c])
                        grid[r][c] = 2
                        fresh -=1
            time +=1


        return time if fresh == 0 else -1
        