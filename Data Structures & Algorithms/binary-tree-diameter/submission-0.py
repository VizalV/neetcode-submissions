# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lefth=self.maxh(root.left)
        righth=self.maxh(root.right)
        diameter=lefth+righth
        subtree=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(diameter,subtree)

    def maxh(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxh(root.left), self.maxh(root.right))

        