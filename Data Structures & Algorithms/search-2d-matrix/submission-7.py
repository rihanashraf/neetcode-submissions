class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
       
        search = l
        while l<=r:
            mid = l+(r-l)//2
            print(mid)
            if matrix[mid][0] < target:
                if matrix[mid][len(matrix[0])-1] >= target:
                    search = mid
                    break
                else:
                    l = mid +1
            elif matrix[mid][0] >target:
               r = mid-1
            else:
                return True


        l = 0
        r = len(matrix[0])-1


        while l<=r:
            m = l+(r-l)//2

            if matrix[search][m] <target:
                l= m+1
            elif matrix[search][m]>target:
                r = m-1
            else:
                return True
        return False
        






































        
            
            
        