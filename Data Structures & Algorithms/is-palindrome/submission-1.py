class Solution:
    def isPalindrome(self, s: str) -> bool:
        #using two point algorithm
        s = s.lower().replace(" ", "")
        s_cleaned = "".join([char for char in s if char.isalnum()])

        
        for i in range(len(s_cleaned)):
            last = s_cleaned[len(s_cleaned)-i-1]
            if s_cleaned[i] != last:
                return False
        return True

