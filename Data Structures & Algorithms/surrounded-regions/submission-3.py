class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # any 'O' island without an edge at the borders is surrounded- find the O regions with connectivity to the edge and add to a set and then remove the rest of the O's which arent in the set

        n,m = len(board), len(board[0])

        def dfs(i,j):
            if (i not in range(n) or j not in range(m) or board[i][j] == "C" or board[i][j] == "X"):
                return

            board[i][j] = "C"

            dfs(i,j-1)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1, j)


        for i in range(n):
            for j in range(m):
                if (i == 0 or j==0 or i == n-1 or j == m-1) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "C":
                    board[i][j] = "O"

                    

        