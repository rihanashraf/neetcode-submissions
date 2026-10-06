class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = heights[0]
        stack = []

        for i in range(len(heights)):
            if not stack or heights[i]>stack[-1][0]:
                stack.append([heights[i], i])
            else:
                while stack and heights[i]<=stack[-1][0]:
                    stackH, stackInd = stack.pop()
                    area = stackH*(i-stackInd)
                    maxarea = max(maxarea, area)

                stack.append([heights[i], stackInd])

            

        for h, i in stack:
            area = h*(len(heights)-i)
            maxarea = max(maxarea, area)

        return maxarea

            
        