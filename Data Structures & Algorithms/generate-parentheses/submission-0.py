class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(o, c, sol):
            if o==n and c==n:
                ans = "".join(sol.copy())
                res.append(ans)
                return
            if o==c:
                sol.append("(")
                backtrack(o+1, c, sol)
                sol.pop()
            if o==n and c<n:
                sol.append(")")
                backtrack(o, c+1, sol)
                sol.pop()

            if o>c and o<n:
                sol.append("(")
                backtrack(o+1, c, sol)
                sol.pop()

                sol.append(")")
                backtrack(o, c+1, sol)
                sol.pop()            
            

        backtrack(0, 0, [])
        return res

                


