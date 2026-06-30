class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #iterate from 1 to max(p)
        import math
        l = 1
        r = max(piles)

        k = float("INF")

        while l <=r:
            m = l+(r-l)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/m)

            if hrs<=h:
                if m<k:
                    k = m
                r = m-1
            else:
                l = m+1
        return k


            


    



                    
            
