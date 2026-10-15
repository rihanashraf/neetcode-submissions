# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res= [0]
        res[0] = 0
        #since its some path related thing, dfs is potentially better
        #characters are non unique
        def dfs(node, maximum):
            if not node:
                return
            if node.val>=maximum:
                res[0]+=1
                maximum = node.val
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, root.val)
        return res[0]
        
        