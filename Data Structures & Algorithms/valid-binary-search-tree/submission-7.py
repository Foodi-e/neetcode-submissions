# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr = []

        def dfs(root):
            if not root: return None

            left = dfs(root.left)
            if root:
                self.arr.append(root.val)
            right = dfs(root.right)
        dfs(root)
        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True




            



