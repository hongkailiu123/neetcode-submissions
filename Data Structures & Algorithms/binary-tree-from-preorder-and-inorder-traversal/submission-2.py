# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {
            value : i
            for i, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index 

            # No nodes in inorder range
            if left > right:
                return None
            
            # The next preorder value in the root
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            split_index = index[root_value]

            root.left = build(left, split_index - 1)
            root.right = build(split_index + 1, right)

            return root
        
        return build(0, len(inorder) - 1)


