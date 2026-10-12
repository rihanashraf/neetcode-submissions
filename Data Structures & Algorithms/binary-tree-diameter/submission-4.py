# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def height(node):
            if not node:
                return 0

            lefth = 1+height(node.left)
            righth = 1+height(node.right)
            total = lefth+righth-1
            self.res = max(self.res, total)
            return max(lefth, righth)

        height(root)
        return self.res-1
        
        
        