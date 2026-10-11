# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append([root, 1])

        if not root:
            return 0

        while q:
            node = q.popleft()
            val = node[0]
            level = node[1]
            if val.left:
                q.append([val.left, level+1])
            if val.right:
                q.append([val.right, level+1])


        return level