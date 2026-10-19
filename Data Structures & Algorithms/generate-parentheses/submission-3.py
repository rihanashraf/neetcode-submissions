class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, sol):
            if o==n and c==n:
                res.append("".join(sol[:]))
                return
            
            if o<n:
                sol.append("(")
                dfs(o+1, c, sol)
                sol.pop()

            if c<o:
                sol.append(")")
                dfs(o, c+1, sol)
                sol.pop()

        dfs(0, 0, [])
        return res                


