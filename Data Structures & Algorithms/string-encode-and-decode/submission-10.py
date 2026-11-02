class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+=str(len(string))
            res+="#"
            res+=string
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<(len(s)):
            length = ""
            while s[i] != "#":
                length +=s[i]
                i+=1
            length = int(length)
            i+=1
            res.append(s[i:i+length])
            i = i+length

        return res



                
         
