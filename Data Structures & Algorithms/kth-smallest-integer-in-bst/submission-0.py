# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrderTraverse(root):
            if not root:
                return []

            return inOrderTraverse(root.left) + [root.val] + inOrderTraverse(root.right)
            
        l = inOrderTraverse(root)
        return l[k - 1]