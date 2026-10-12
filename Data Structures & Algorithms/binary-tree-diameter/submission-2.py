# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.h = 0
        def tree_height(root):
            if not root: return 0

            left = tree_height(root.left)
            right = tree_height(root.right)
            if right + left > self.h:
                self.h = right + left

            return 1 + max(left, right)
        tree_height(root)

        return self.h
        
                

