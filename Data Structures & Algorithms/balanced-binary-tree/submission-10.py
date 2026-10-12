# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #need to return a bool

        def dfs(root):
            if not root:
                return 0

            l,r = dfs(root.left), dfs(root.right)
            if l!=-1 and r!=-1 and (abs(l-r)<=1):
                return 1+max(l, r)
            return -1

        return dfs(root)!=-1
        