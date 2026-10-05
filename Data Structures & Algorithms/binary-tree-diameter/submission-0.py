# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        def dfs(curr_root):
            if not curr_root: return 0

            left = dfs(curr_root.left)
            right = dfs(curr_root.right)
            
            if left+right > self.res: 
                self.res = left+right

            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        






