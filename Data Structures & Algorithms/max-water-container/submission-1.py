class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0,n-1

        maximum  = 0

        while i <j:
            area = min(heights[i], heights[j])*(j-i)
            maximum = max(maximum, area)

            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
            
        return maximum
        