"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfs(n, visited):
            if not n:
                return None

            if n.val in visited: #this was tough, I had to keep dict instead
                return visited[n.val] #of set, so whenever, I revisit a node
                    #I can return its already created clone and return early             

            clone = Node(n.val, [])
            visited[n.val] = clone

            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor, visited))

            return clone

        return dfs(node, {})