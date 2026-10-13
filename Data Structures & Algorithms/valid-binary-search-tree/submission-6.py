# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # max_possible_value_on_left
        # min_possible_value_on_right
        #if not root: return True
        # q = collections.deque()
        # q.append(root)
        # while q:
        #     l = len(q)
        #     for i in range(l):
        #         node = q.popleft()

        #         if node.left:
        #             if node.left.val >= node.val:
        #                 return False
        #             q.append(node.left)

        #         if node.right:
        #             if node.right.val <= node.val:
        #                 return False
        #             q.append(node.right)
        # return True

        self.arr = []

        def dfs(root):
            if not root: return None

            left = dfs(root.left)
            if left:
                self.arr.append(left.val)
            if root:
                self.arr.append(root.val)
            right = dfs(root.right)
            if right:
                self.arr.append(right.val)
        dfs(root)
        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True




            



