class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea =0
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

        #after everything completes
        while stack:
            stackH, stackInd = stack.pop()
            maxarea = max(maxarea, stackH*(len(heights)-stackInd))

        return maxarea
            

            
        