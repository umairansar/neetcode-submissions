# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # just without comments, use range
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, l, r):
            if not root:
                return True

            if root.right and root.val >= root.right.val:
                return False
            elif root.left and root.val <= root.left.val:
                return  False
            elif root.val <= l or root.val >= r:
                return False
            
            return isValid(root.left, l, root.val) and \
                   isValid(root.right, root.val, r)

        return isValid(root, -1001, 1001)