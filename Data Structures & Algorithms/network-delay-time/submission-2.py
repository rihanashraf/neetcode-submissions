class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append([w, v])


        minH = [[0, k]]
        visit = set()
        res =0
        while minH:
            weight, node = heapq.heappop(minH)
            if node in visit:
                continue
            res = max(res, weight)
            visit.add(node)

            for neiw, nei in edges[node]:
                if nei in visit:
                    continue
                heapq.heappush(minH, [neiw+weight, nei])

        
        return res if len(visit) == n else -1


        
