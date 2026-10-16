# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #iteratively how?
        maximum = 1
        height = 1
        if not root:
            return 0
        stack = [[root, height]]

        while stack:
            node, height = stack.pop()
            if node.left:
                stack.append([node.left, height+1])
                maximum = max(maximum, height+1)
            if node.right:
                stack.append([node.right, height+1])
                maximum = max(maximum, height+1)

        return maximum

