# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max = 0
    cnt = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return self.max
        self.cnt+=1
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        if self.cnt > self.max: self.max = self.cnt
        self.cnt -= 1

        return self.max


