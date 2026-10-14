# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        c = root

        if (p.val > c.val and q.val <c.val) or (p.val<c.val and q.val>c.val):
            return c

        elif c.val == p.val or c.val == q.val:
            return c

        elif p.val<c.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        else:
            return self.lowestCommonAncestor(root.right, p, q)


        


        