class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        from collections import deque
        seen = set()
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        length = 1
        while q:
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if 0<=row<n and 0<=col<m and (row, col) not in seen and grid[row][col] == 2147483647:
                        grid[row][col] = length
                        q.append((row, col))
                        seen.add((row, col))
            length +=1

