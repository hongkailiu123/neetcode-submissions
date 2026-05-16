# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
            
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            left = node.left
            right = node.right
            node.left = right
            node.right = left

            if left:
                q.append(left)
            
            if right:
                q.append(right)
            
        
        return root


        




        