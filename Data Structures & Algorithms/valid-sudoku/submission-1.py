class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row, column and 3*3 grid
        n, m = len(board), len(board[0])
    
        #rows   
        for i in range(n):
            seen  =set()
            for j in range(m):
                if board[i][j] in seen:
                    return False
                if board[i][j]!=".":
                    seen.add(board[i][j]) 

                
        #columns    
        for i in range(n):
            seen = set()
            for j in range(m):
                if board[j][i] in seen:
                    return False
                if board[j][i]!=".":
                    seen.add(board[j][i]) 

        #3*3
        x = 0
        y = 0

        while x+3<10 and y+3<10:
            seen = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] in seen:
                        return False
                    if board[i][j]!=".":
                        seen.add(board[i][j]) 
            y+=3
            if y == 9:
                y =0
                x+=3

        return True
        

        
        