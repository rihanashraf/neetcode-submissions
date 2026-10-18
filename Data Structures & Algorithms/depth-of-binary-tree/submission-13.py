# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        height = 1
        stk = [[root, 1]]
        if not root:
            return 0

        while stk:
            node, height = stk.pop()
            maximum = max(maximum, height)
            if node.right:
                stk.append([node.right, height+1])
            
            if node.left:
                stk.append([node.left, height+1])
        return maximum


