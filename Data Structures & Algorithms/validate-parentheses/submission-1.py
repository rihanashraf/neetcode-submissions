class Solution:
    def isValid(self, s: str) -> bool:
        dicti = {")":"(", "}":"{", "]": "["}

        stk =[]
        for char in s:
            if char not in dicti:
                stk.append(char)
            else:
                if stk:
                    popped = stk.pop()
                    if dicti[char] != popped:
                        return False
                else:
                    return False
        return True if not stk else False