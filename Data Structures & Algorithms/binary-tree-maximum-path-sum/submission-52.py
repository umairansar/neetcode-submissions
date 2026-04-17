# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            # nonlocal paths
            if not root:
                return

            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
            
            #0 => L+R+Parent, 
            #1 => maxLR+Parent
            just_l = root.left.val[0] if root.left else root.val
            just_r = root.right.val[0] if root.right else root.val
            l = max(root.left.val[1], 0) if root.left else 0
            r = max(root.right.val[1], 0) if root.right else 0
            lr = root.val + l + r
            maxlr = root.val + max(l, r)
            root.val = (max(lr, just_l, just_r), maxlr)

        traverse(root)
        return root.val[0]
