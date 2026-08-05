# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number_good = 0
        def dfs(node, maxsf):
            nonlocal number_good
            if not node:
                return
            
            if node.val >= maxsf:
                number_good += 1
            
            dfs(node.left, max(node.val, maxsf))
            dfs(node.right, max(node.val, maxsf))
            return 
        
        dfs(root, root.val)
        return number_good

            
            

            


        