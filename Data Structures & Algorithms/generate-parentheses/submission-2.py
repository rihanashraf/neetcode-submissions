class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(o, c, sol):
            if o==n and c==n:
                ans = "".join(sol)
                res.append(ans)
                return
            if o<n:
                sol.append("(")
                backtrack(o+1, c, sol)
                sol.pop()
            if c<o:
                sol.append(")")
                backtrack(o, c+1, sol)
                sol.pop()            

        backtrack(0, 0, [])
        return res

                


