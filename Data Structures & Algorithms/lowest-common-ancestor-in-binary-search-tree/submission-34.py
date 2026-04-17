# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pAncestors = self.findAncestors(root, p, [])
        qAncestors = self.findAncestors(root, q, [])
        print(pAncestors[0].val, qAncestors[0].val)
        length = min(len(qAncestors), len(pAncestors))
        for i in range(length):
            if pAncestors[i].val == qAncestors[i].val:
                if i == length - 1:
                    return pAncestors[i]
                else:
                    pass
            else:
                return pAncestors[i - 1]

    def findAncestors(self, root: TreeNode, node: TreeNode, ans: List[TreeNode]) -> List[TreeNode]:
        if not root:
            return []

        if node.val == root.val:
            print("match> ", root.val)
            ans.append(node)
            return ans
        else:
            ans.append(root)
            if node.val > root.val:
                print("find right> ", node.val, root.val)
                return self.findAncestors(root.right, node, ans)
            else:
                print("find left> ", node.val, root.val)
                return self.findAncestors(root.left, node, ans)

        
