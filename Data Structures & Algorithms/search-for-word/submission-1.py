class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for every node on the grid, if it starts with 
        n,m = len(board), len(board[0])
        seen = set()

        def dfs(i, j, word, string, seen):
            if string == word:
                return True
            l = len(string)
            if string[l-1]!=word[l-1]:
                return False
            if len(string)>len(word):
                return False

            dirs =[[0, -1], [0, 1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                r, c = i+dr, j+dc
                if 0<=r<n and 0<=c<m and (r, c) not in seen:
                    string+=board[r][c]
                    seen.add((r,c))
                    if dfs(r,c, word, string, seen):
                        return True
                    string = string[:-1]
                    seen.remove((r, c))


        for i in range(n):
            for j in range(m):
                seen = set()
                seen.add((i,j))
                if board[i][j] == word[0]:
                    if dfs(i, j, word, board[i][j], seen):
                        return True

        return False
            
        
        