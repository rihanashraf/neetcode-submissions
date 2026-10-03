class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force is O(n^2)
        n = len(temperatures)
        output = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i]>stack[-1][0]:
                index = stack[-1][1]
                output[index] = i - index
                stack.pop()

            stack.append([temperatures[i], i])
            

        return output
        
        