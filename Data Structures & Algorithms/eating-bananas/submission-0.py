class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #iterate from 1 to max(p)

        import math

        maximum = max(piles)
        l =1
        r = max(piles)

        mini = 1

        

        while l<=r:
            k = l+(r-l)//2
            hr = 0
            for pile in piles:
                hr += math.ceil(pile/k)
                print(hr)
            if hr<=h:
                mini = k
                r = k-1
            else:
                l = k+1

        return mini


            


    



                    
            
