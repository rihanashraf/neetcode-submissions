class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 1

        for i in range(n-1):
            temp = y
            y = x+y
            x = temp
        return y