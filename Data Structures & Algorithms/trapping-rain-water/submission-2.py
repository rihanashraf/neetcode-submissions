class Solution:
    def trap(self, height: List[int]) -> int:

        #at every index, we need the maxL and maxR
        if not height:
            return 0
        n = len(height)
        l, r = 0, n-1
        maxl, maxr = height[l], height[r]
        res = 0

        while l<r:
            if maxl>maxr:
                r-=1
                maxr = max(maxr, height[r])
                res += maxr - height[r]

            else:
                l+=1
                maxl = max(maxl, height[l])
                res+= maxl-height[l]

        return res
                

            

            
            


        
        

        


            
        