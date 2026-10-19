class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for every node on the grid, if it starts with 
        n, m = len(board), len(board[0])
        seen = set()

        def dfs(r, c, string):
            if string == word:
                return True

            if r<0 or r>=n or c<0 or c>=m or (r,c) in seen:
                return False

            string+=board[r][c]
            l = len(string)
            if board[r][c] != word[l-1]:
                return False

            seen.add((r,c))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                i, j = r+dr, c+dc
                if dfs(i, j, string):
                    return True
            string = string[:-1]
            seen.remove((r,c))

        for i in range(n):
            for j in range(m):
                if dfs(i, j, ""):
                    return True


        return False

            
        
        
        