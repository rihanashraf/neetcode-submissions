class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}

        for char in s:
            if char in dicti:
                dicti[char]+=1
            else:
                dicti[char] = 1
        
        for char in t:
            if char in dicti and dicti[char]>0:
                dicti[char] -=1
            else:
                return False
        return True if len(s) == len(t) else False
        