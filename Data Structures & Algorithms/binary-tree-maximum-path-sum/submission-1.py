# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum_so_far = None

        def dfs(node) -> int:
            nonlocal maximum_so_far
            if not node:
                return 0
            
            left_path_sum = max(0, dfs(node.left))
            right_path_sum = max(0, dfs(node.right))

            current_path_sum = node.val + left_path_sum + right_path_sum
            if maximum_so_far is None or maximum_so_far < current_path_sum:
                maximum_so_far = current_path_sum
            
            return node.val + max(left_path_sum, right_path_sum)
        
        dfs(root)
        return maximum_so_far




        