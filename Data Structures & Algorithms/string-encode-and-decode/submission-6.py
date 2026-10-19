class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for char in strs:
            res+=str(len(char))
            res+="#"
            res+=char
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j= i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            string =""
            i= j+1
            if i >len(s):
                break
            for j in range(i, i+length):
                string+=s[j]
                i+=1
            res.append(string)
        return res
                
         
