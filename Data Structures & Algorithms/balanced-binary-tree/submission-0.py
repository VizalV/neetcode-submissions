# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        if self.getHeight(root)==-1:
            return False
        else:
            return True


    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_tree=self.getHeight(root.left)
        right_tree=self.getHeight(root.right)
        if left_tree==-1 or right_tree==-1:
            return -1
        elif abs(left_tree-right_tree)>1:
            return -1
        return 1+max(left_tree,right_tree)