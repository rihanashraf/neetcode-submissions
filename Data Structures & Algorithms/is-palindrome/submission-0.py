class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        for letter in s:
            if letter.isalnum():
                string += letter
        s = string

        for i in range(len(s)):
            j = -i-1
            if s[i] != s[j]:
                return False
        return True