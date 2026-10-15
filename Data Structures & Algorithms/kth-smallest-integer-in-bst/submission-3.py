# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #the smallest value is in the left most to the left
        smallest=float("inf")
        i = 0
        def dfs(node):
            nonlocal smallest
            nonlocal i
            if not node:
                return
            dfs(node.left)
            if i>=k:
                return
            smallest =node.val
            i+=1
            dfs(node.right)
            
        dfs(root)

        return smallest


        