# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(curr_root):
            if not curr_root: return 0

            left = height(curr_root.left)
            right = height(curr_root.right)

            if math.fabs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)

        height(root)

        return self.balanced

