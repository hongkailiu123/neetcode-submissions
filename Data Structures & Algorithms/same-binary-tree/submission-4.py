# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            #-101 means None
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False

            left_same = dfs(node1.left, node2.left)
            right_same = dfs(node1.right, node2.right)

            if node1.val == node2.val and left_same and right_same:
                return True
            else:
                return False
        
        return dfs(p, q)