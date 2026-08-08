# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        if root:    
            q.append(root)

        while q:
            length = len(q)
            right = 0
            for i in range(length):
                node = q.popleft()
                right = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(right)
        
        return res