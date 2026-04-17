# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ctr = 0

        def dfs(root):
            nonlocal ctr
            if not root:
                return None
            
            res = dfs(root.left)
            if res:
                return res

            ctr += 1

            if ctr == k:
                return root
            
            res = dfs(root.right)
            if res:
                return res

            return None

        res = dfs(root)
        return res.val
