class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        seen = set()

        def dfs(i, j, seen):
            seen.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen and board[r][c] == "O":
                    seen.add((r, c))
                    dfs(r, c, seen)


        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0, seen)
            if board[i][m-1] == "O":
                dfs(i, m-1, seen)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j, seen)
            if board[n-1][j] == "O":
                dfs(n-1, j, seen)

        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"