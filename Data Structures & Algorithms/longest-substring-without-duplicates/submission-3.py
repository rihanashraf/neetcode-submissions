class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1

        i, j = 0, 0

        longest = 0
        length = 0

        dicti = {}

        while i <len(s):
            if s[i] in dicti and dicti[s[i]]>=j:
                j = dicti[s[i]]+1
                dicti[s[i]] = i
                length = (i-j)+1
                i+=1
            else:
                length +=1
                longest = max(longest, length)
                dicti[s[i]] = i
                i+=1

        longest = max(longest, length)
        return longest
                
            
        