# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu = deque()
        qu.append([p, q])

        while qu:
            p, q = qu.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val!=q.val:
                return False          
            qu.append([p.left, q.left])
            qu.append([p.right, q.right])

        return True        

        
        
        