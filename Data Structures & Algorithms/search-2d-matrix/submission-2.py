class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m-1

        while l <= r:
            mid = l + (r-l)//2
            x = matrix[mid]
            if x[0] == target:
                return True
            elif target > x[0]:
                l = mid +1
            else:
                r= mid-1
        midd = r

        l = 0
        r = n-1

        while l <= r:
            middd = l + (r-l)//2
            y = matrix[midd]
            if y[middd] == target:
                return True
            elif target > y[middd]:
                l = middd+1
            else:
                r = middd-1
        
        return False



