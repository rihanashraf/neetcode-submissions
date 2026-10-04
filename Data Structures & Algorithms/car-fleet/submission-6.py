class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedDict = {}
        for i in range(len(position)):
            speedDict[position[i]] = speed[i]

        position.sort()
        l = len(position)

        stack = []
        
        for i in range(l-1, -1, -1):
            time = (target-position[i])/speedDict[position[i]]
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
            

        





        
        


        