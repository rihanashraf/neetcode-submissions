class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedDict = {}
        for i in range(len(position)):
            speedDict[position[i]] = speed[i]

        position.sort()
        l = len(position)

        timeDict = {}

        for i in range(l-1, -1, -1):
            timeDict[position[i]] = (target-position[i])/(speedDict[position[i]])

        output = 1
        stack = []
        
        for i in range(l-1, -1, -1):
            if stack and timeDict[position[i]]>stack[-1][1]:
                output+=1
            while stack and timeDict[position[i]]>stack[-1][1]:
                stack.pop()

            if stack:
                stack.append([position[i], stack[-1][1]])
            else:
                stack.append([position[i], timeDict[position[i]]])

        return output
            

        





        
        


        