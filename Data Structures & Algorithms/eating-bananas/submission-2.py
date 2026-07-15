class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #koko eating bananas

        mink = 0
        import math

        l=1
        r = max(piles)
        while l<=r:
            m = l+(r-l)//2
            hrs = 0
            for pile in piles:
                hrs+=math.ceil(pile/m)
            print(hrs)
            if hrs<=h:
                r = m-1
                mink = m
            else:
                l= m+1
        return mink
            


        