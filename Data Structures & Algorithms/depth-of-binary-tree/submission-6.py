# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        stack.append([root,1])

        maximum = 0

        while stack:
            node = stack.pop()
            val = node[0]
            level = node[1]
            maximum = max(maximum, level)
            if val.left:
                stack.append([val.left, level+1])
            if val.right:
                stack.append([val.right, level+1])

        return maximum