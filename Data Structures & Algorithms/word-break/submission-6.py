class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #couple of things - dp[len(s)]= True is the base case
        #also we check all the words in wordDict instead of the other way around
        #how to solve this recursively?

        dp = {len(s) : True}

        def check(i):
            if i in dp:
                return dp[i]

            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)] == w:
                    dp[i] = check(i+len(w))
                if i in dp and dp[i]:
                    break
            if i not in dp:
                dp[i] = False

            return dp[i]


        return check(0)


