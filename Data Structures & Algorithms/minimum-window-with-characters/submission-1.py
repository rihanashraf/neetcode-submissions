class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        #basically, for this problem, i need to have two hashmaps

        if t == "": return ""
        static = {}
        for char in t:
            static[char] = 1+static.get(char, 0)

        need = len(static)

        dynamic = {}
        have = 0 
        j = 0

        res, resLen = [-1, -1], float("inf")

        for i in range(len(s)):
            if s[i] in static:
                dynamic[s[i]] = 1+dynamic.get(s[i], 0)
                if dynamic[s[i]] == static[s[i]]:
                    have+=1

            while have==need:
                length = i-j+1
                if length <resLen:
                    resLen = length
                    res = [j, i]
                if s[j] in static:
                    dynamic[s[j]]-=1
                    if dynamic[s[j]]<static[s[j]]:
                        have-=1
                j+=1

        if resLen !=float("inf"):
            return s[res[0]:res[1]+1]
        return ""





                






        

            







        
        