class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 2
        if n==1:
            return 1
        if n==2:
            return 2
        
        for i in range(3, n+1):
            temp =y
            y = x+y
            x = temp
        
        return y