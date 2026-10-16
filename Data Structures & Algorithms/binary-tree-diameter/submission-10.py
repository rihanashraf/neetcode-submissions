# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [1]
        res[0] = 0

        def height(node):
            if not node:
                return 0
            res[0] = max(res[0], height(node.left)+height(node.right))
            return 1+max(height(node.left), height(node.right))
        height(root)
        return res[0]

        
        
        