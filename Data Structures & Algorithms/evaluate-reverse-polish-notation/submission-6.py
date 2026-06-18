class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dict = {"+":1, "-":1, "*":1, "/":1}
        stk = []
        ans = int(tokens[0])
        stk.append(int(tokens[0]))

        for i in range(1, len(tokens)):
            if tokens[i] not in dict:
                stk.append(int(tokens[i]))        
            else: 
                if tokens[i] == "+":
                    one = stk.pop()
                    two = stk.pop()
                    ans = one+two
                    stk.append(ans)

                if tokens[i] == "-":
                    one = stk.pop()
                    two = stk.pop()
                    ans = two -one
                    stk.append(ans)

                if tokens[i] == "*":
                    one = stk.pop()
                    two = stk.pop()
                    ans = two *one
                    stk.append(ans)
                
                if tokens[i] == "/":
                    one = stk.pop()
                    two = stk.pop()
                    ans = int(two / one)
                    stk.append(ans)
                print(stk)

        return ans
                
