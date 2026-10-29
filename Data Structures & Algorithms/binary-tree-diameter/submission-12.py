# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def height(node):
            if not node:
                return 0
            lefth = height(node.left)
            righth = height(node.right)
            res[0] = max(res[0], lefth+righth)
            return 1+max(lefth, righth)

        height(root)
        return res[0]
        
        
        