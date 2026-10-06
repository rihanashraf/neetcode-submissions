class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicti ={}

        for char in s1:
            if char not in dicti:
                dicti[char]=1
            else:
                dicti[char]+=1

        def perm(i, j):
            copy = dicti.copy()
            while i<j:
                if s2[i] in copy and copy[s2[i]]==0:
                    return False
                elif s2[i] in copy:
                    copy[s2[i]] -=1
                else:
                    return False
                
                i+=1
            return True
        

        for i in range(len(s2)-len(s1)+1):
            if s2[i] in dicti and perm(i, i +len(s1)):
                return True

        return False


        


        