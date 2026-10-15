# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #the smallest value is in the left most to the left
        smallest=[0]*k
        i = 0
        def dfs(node):
            nonlocal i
            if not node:
                return
            dfs(node.left)
            if i>=k:
                return
            smallest[i]=node.val
            i+=1
            dfs(node.right)
            return
            
        dfs(root)

        return smallest[k-1]


        