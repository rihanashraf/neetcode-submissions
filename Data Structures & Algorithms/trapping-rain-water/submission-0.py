class Solution:
    def trap(self, height: List[int]) -> int:

        #at every index, we need the maxL and maxR

        maxl = [0]*(len(height))
        maxl[0] = 0
        for i in range(1, len(height)):
            maxl[i] = max(maxl[i-1], height[i-1])

        maxr = [0]*len(height)
        maxr[len(height)-1] = 0
        for i in range(len(height)-2, -1, - 1):
            maxr[i] = max(maxr[i+1], height[i+1])

        res = 0
        
        for i in range(len(height)):
            diff = min(maxr[i], maxl[i]) - height[i]
            
            if diff>0:
                res+=diff


        return res


        


            
        