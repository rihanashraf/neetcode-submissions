class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need to group anagrams together into sub lists
        #all anagrams have same counts

        from collections import Counter
        seen = {}
        out = []
        for s in strs:
            count = [0]*26
            for x in s:
                count[ord(x)-ord("a")] +=1
            l = tuple(count)
            
            if l in seen:
                out[seen[l]].append(s)
            else:
                out.append([s])
                seen[l] = len(out)-1

        return out
