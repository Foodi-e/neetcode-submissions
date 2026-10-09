# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(root, max_path):
            if not root: return None
            if root.val >= max_path:
                max_path = root.val
                self.cnt += 1
            dfs(root.left, max_path)
            dfs(root.right, max_path)
        dfs(root, root.val)
        return self.cnt
            
