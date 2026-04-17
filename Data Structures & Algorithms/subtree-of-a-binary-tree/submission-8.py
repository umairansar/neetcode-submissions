# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        elif root == None:
            return False
        elif subRoot == None:
            return False

        if root.val != subRoot.val:
            res = self.isSubtree(root.left, subRoot)
            res = res or self.isSubtree(root.right, subRoot)
            return res
        else:
            res = self.isSubtree(root.left, subRoot)
            res = res or self.isSubtree(root.right, subRoot)
            resMust = self.isSubtreeMust(root.left, subRoot.left)
            resMust = resMust and self.isSubtreeMust(root.right, subRoot.right)
            return res or resMust

    def isSubtreeMust(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        elif root == None:
            return False
        elif subRoot == None:
            return False

        if root.val != subRoot.val:
            return False
        else:
            res = self.isSubtreeMust(root.left, subRoot.left)
            res = res and self.isSubtreeMust(root.right, subRoot.right)
            return res

