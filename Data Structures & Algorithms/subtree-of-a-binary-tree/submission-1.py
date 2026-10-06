# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True

        def equivalent(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val is not root2.val: return False
            
            return (
                equivalent(root1.left, root2.left) and 
                equivalent(root1.right, root2.right)
            )
        
        if not root: return False
        if root.val is subRoot.val: 
            if equivalent(root, subRoot): return True
        
        return (    
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )



                        


        