# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #how to do using iterative bfs

        qu = deque()
        qu.append((p, q))
        c = 0

        while qu:
            i, j = qu.popleft()
            if not i and not j:
                continue
            if not i or not j or i.val!=j.val:
                return False
            qu.append((i.left, j.left))
            qu.append((i.right, j.right))

        return True            

        
        
        