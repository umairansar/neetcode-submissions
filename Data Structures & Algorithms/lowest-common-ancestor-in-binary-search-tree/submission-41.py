# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #find all ancestors, then find last common one
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pAncestors = self.findAncestors(root, p, [])
        qAncestors = self.findAncestors(root, q, [])
        
        length = min(len(qAncestors), len(pAncestors))
        for i in range(length):
            if pAncestors[i].val == qAncestors[i].val:
                pass
            else:
                return pAncestors[i - 1]

        return pAncestors[i]

    def findAncestors(self, root: TreeNode, node: TreeNode, ans: List[TreeNode]) -> List[TreeNode]:
        if not root:
            return []

        if node.val == root.val:
            ans.append(node)
            return ans
        else:
            ans.append(root)
            if node.val > root.val:
                return self.findAncestors(root.right, node, ans)
            else:
                return self.findAncestors(root.left, node, ans)

        
