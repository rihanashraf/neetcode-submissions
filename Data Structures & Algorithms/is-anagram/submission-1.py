class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        for letter in s:
            if letter not in dicti:
                dicti[letter] = 1
            else:
                dicti[letter] +=1
        
        for letter in t:
            if letter in dicti and dicti[letter] >0:
                dicti[letter] -=1
            else:
                return False
        return True if len(s) == len(t) else False
        