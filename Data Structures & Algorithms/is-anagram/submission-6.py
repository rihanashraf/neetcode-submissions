class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}

        for char in s:
            countS[char] = 1+countS.get(char, 0)

        for char in t:
            if char in countS and countS[char]>0:
                countS[char] -=1

            else:
                return False
            

        return True if len(s)==len(t) else False
