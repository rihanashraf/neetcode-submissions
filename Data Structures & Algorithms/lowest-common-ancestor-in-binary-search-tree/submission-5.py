# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
         c = root
         
         while c:
            if c.val <p.val and c.val <q.val:
                c = c.right
            elif c.val>p.val and c.val>q.val:
                c = c.left
            else:
                return c


        


        