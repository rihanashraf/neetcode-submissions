class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])
                if number<=0 or number>9 or number in seen:
                    return False
                seen.add(number)

        #column
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                number = int(board[j][i])
                if number<=0 or number>9 or number in seen:
                    return False
                seen.add(number)

        #3x3 grid

        n,m = 0, 1
        s,r = 0, 1
        while n<3:
            seen = set()
            for i in range(3*n, 3*m):   
                for j in range(3*s, 3*r):
                    if board[i][j] == ".":
                        continue
                    number = int(board[i][j])
                    if number<=0 or number>9 or number in seen:
                        return False
                    seen.add(number)        
            s+=1
            r+=1
            if s==3:
                s, r = 0, 1
                n+=1
                m+=1


        return True

                
            

        
        