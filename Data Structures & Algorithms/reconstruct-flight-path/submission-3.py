class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # Reverse sort so we can pop the smallest destination
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                nei = adj[src].pop()
                dfs(nei)

            res.append(src)

        dfs("JFK")

        return res[::-1]

        

        