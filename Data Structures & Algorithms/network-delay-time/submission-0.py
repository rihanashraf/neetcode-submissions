class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((w, v))
        visit = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, w1)

            for w2, n2 in edges[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minHeap, (w1+w2, n2))


        return res if len(visit) == n else -1
        
        