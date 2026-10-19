class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}

        for char in s:
            countS[char] = 1+countS.get(char, 0)


        for char in t:
            if char not in countS or countS[char]<=0:
                return False

            countS[char]-=1


        return True if len(s) == len(t) else False