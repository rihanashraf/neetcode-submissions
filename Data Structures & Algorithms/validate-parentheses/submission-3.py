class Solution:
    def isValid(self, s: str) -> bool:
        dicti = {"{": "}", "[": "]", "(":")"}
        stk= []

        for char in s:
            if char in dicti:
                stk.append(char)
                continue
            
            if not stk and char not in dicti:
                return False
            n = stk.pop()
            if dicti[n] != char:
                return False

        return True if not stk else False
        

