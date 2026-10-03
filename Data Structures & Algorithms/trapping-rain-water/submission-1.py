class Solution:
    def trap(self, height: List[int]) -> int:

        #at every index, we need the maxL and maxR
        n = len(height)
        maxl = height[0]
        maxr = height[n-1]
        l, r = 0, n-1
        res = 0

        while l<r:
            if maxl>maxr:
                r-=1
                diff = min(maxl, maxr) - height[r]
                maxr = max(maxr, height[r])

            else:
                l+=1
                diff = min(maxl, maxr) - height[l]
                maxl = max(maxl, height[l])

            if diff>0:
                res+=diff

        return res
                

            

            
            


        
        

        


            
        