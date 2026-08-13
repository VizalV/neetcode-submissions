# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def isSameTree(self,root,sub):
        if root is None and sub is None:
            return True
        if root and sub and root.val==sub.val:
            return (self.isSameTree(root.left,sub.left) and
            self.isSameTree(root.right,sub.right))
        
        return False


