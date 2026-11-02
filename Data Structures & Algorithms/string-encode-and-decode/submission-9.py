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
        print(s)
        while i<(len(s)):
            length = ""
            while s[i] != "#":
                length +=s[i]
                i+=1
            length = int(length)
            print(length)
            j = i+1
            maxi = j+length
            curr = ""
            while j!=maxi:
                curr+=s[j]
                j+=1
            res.append(curr)
            i = j

        return res



                
         
