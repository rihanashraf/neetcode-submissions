class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for every node on the grid, if it starts with 
        n, m = len(board), len(board[0])
        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r<0 or r>=n or c<0 or c>=m or (r,c) in seen or board[r][c]!= word[i]:
                return False

            seen.add((r,c))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                a, j = r+dr, c+dc
                if dfs(a, j, i+1):
                    return True
            seen.remove((r,c))

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True


        return False

            
        
        
        