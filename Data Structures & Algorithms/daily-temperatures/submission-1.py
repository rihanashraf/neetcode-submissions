class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(N) time and O(n) space.
        stk = []
        output = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t>stk[-1][0]:
                temp, index = stk.pop()
                output[index] = i-index
            if stk and t<=stk[-1][0]:
                stk.append([t, i])
            if not stk:
                stk.append([t, i])
        while stk:
            temp, index = stk.pop()
            output[index] = 0
        return output


            