# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        maximum = 0

        while stack:
            node, level = stack.pop()
            if node:
                maximum = max(maximum, level)
                stack.append([node.right, level+1])
                stack.append([node.left, level+1])

        return maximum