class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicti = {}

        res = 0 
        l = 0

        for r in range(len(s)):
            
            if s[r] in dicti:
                dicti[s[r]]+=1
            else:
                dicti[s[r]]=1
            
            rep = (r-l+1) -(max(dicti.values()))
    

            if rep >k:
                dicti[s[l]] -=1
                l+=1

            res = max(res, r-l+1)
            

        return res


        