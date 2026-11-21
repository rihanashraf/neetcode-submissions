class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets = sorted(tickets, reverse=True)

        for u,v in tickets:
            adj[u].append(v)

        out = []

        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
                
            out.append(node)


        dfs("JFK")
        return out[::-1]      

        