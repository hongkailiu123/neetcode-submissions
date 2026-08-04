# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        large, small = None, None
        if p.val > q.val:
            large = p
            small = q
        else:
            large = q
            small = p
        
        if small.val < root.val and large.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif small.val > root.val and large.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


        
        