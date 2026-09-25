class Solution:
    def longestPalindrome(self, s: str) -> str:

        # need to handle odd and even strings separately
        res_l = 0
        res_r = 0
        leng = 0

        for i in range(len(s)):
            #odd
            l,r = i, i 
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > leng:
                    res_l= l
                    res_r = r
                    leng = r-l+1
                l-=1
                r+=1

            #even 
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > leng:
                    res_l = l
                    res_r= r
                    leng = r-l+1
                l-=1
                r+=1

        return s[res_l:res_r+1]




        
        
        
        