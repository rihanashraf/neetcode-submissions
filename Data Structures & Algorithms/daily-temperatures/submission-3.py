class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(N) time and O(n) space.
        stk = []
        output = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t>stk[-1][0]:
                temp, index = stk.pop()
                output[index] = i-index
            stk.append([t, i])
        return output


            