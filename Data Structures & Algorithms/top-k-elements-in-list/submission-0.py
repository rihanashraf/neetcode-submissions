class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        for n in nums:
            if n not in dicti:
                dicti[n] = 1
            else:
                dicti[n]+=1
        
        arr = [[] for i in range(len(nums)+1)]
        for key, value in dicti.items():
            arr[value].append(key)
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) ==k:
                    return res