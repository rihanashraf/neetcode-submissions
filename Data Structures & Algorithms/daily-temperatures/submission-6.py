class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force is O(n^2)
        n = len(temperatures)
        output = [0]*n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd

            stack.append([t, i])
            
        return output
        
        