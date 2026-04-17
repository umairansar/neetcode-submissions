# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return "None"
        
        def preorder(r):
            if not r:
                return "n"

            if r.val:
                return str(r.val) + "," + preorder(r.left) + "," + preorder(r.right)

        s = preorder(root)
        print(s)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == "None":
            return TreeNode("")
    
        def preorder(r):
            if len(s) <= 0:
                return

            if s[0] != "n":
                r.left = TreeNode(s.pop(0))
                preorder(r.left)
            else:
                s.pop(0)


            if s[0] != "n":
                r.right = TreeNode(s.pop(0))
                preorder(r.right)
            else:
                s.pop(0)

        s = data.split(",")
        root = TreeNode(s.pop(0))
        preorder(root)
        return root
        
