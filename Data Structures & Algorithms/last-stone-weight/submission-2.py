class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x==y:
                continue
            heapq.heappush(stones, -abs(y-x))

        if not stones:
            return 0
        return -stones[0]



        