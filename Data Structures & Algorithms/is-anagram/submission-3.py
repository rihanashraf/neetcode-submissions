class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        for i in s:
            if i not in dicti:
                dicti[i]=1
            else:
                dicti[i] += 1

        for j in t:
            if j in dicti and dicti[j]!=0:
                dicti[j] -=1
            else:
                return False

        return True if len(s) == len(t) else False
            