# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(p, i, res):
            rootIdxI = i.index(res.val)
            
            i_l = i[:rootIdxI]
            i_r = i[rootIdxI+1:]

            size_l = len(i_l)
            p_l = p[1:1+size_l]
            p_r = p[1+size_l:]

            if len(i_l) > 0:
                res.left = TreeNode(p_l[0])
                dfs(p_l, i_l, res.left)
            
            if len(i_r) > 0:
                res.right = TreeNode(p_r[0])
                dfs(p_r, i_r, res.right)
        
        res = TreeNode(preorder[0])
        dfs(preorder, inorder, res)
        return res