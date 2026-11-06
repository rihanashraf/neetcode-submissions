class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sort it with a tuple kind of
        import heapq
        arr = []
        for xi, yi in points:
            dyn = []
            dyn.append(xi**2+yi**2)
            dyn.append([xi, yi])
            arr.append(dyn)

        heapq.heapify(arr)

        out = []
        for i in range(k):
            e = heapq.heappop(arr)
            out.append(e[1])

        return out

        


