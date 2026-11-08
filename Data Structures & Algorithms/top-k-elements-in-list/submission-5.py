class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort i know this, we need the top 2 occuring values

        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1+count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)

        out = []
        for i in range(len(freq)-1, -1, -1):

            for x in freq[i]:
                out.append(x)
                if len(out) ==k:
                    return out



        
        
        