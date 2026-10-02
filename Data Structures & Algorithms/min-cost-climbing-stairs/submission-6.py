class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        x = cost[0]
        y = cost[1]

        for i in range(2, n):
            temp = y
            y = min(y+cost[i], x+cost[i])
            x = temp

        return min(x, y)
        
            
