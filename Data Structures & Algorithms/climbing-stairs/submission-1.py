class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 1
        if n ==0:
            return 0
        elif n==1:
            return 1
        
        for i in range(2, n+1):
            temp =y
            y = x+y
            x = temp
        
        return y