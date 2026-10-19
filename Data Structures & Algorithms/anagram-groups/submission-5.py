class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp = [""]*len(strs)
        output = []
        
        for i in range(len(strs)):
            comp[i] = "".join(sorted(strs[i]))

        dicti = {}
        i = 0
        for j in range(len(comp)):
            if comp[j] not in dicti:
                dicti[comp[j]] = i
                i+=1
        for i in range(len(dicti)):
            output.append([])
        for i in range(len(strs)):
            output[dicti[comp[i]]].append(strs[i])
            
            
        return output





        