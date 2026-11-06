class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #the weight of the last remaning stone is to be returned
        import heapq

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) >1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x<y:
                heapq.heappush(stones, x-y)


        return -stones[0] if stones else 0


        