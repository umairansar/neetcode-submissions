class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        path = self.root
        for i, c in enumerate(word):
            if c not in path.children:
                path.children[c] = TrieNode()
            if i == len(word) - 1:
                path.children[c].eow = True
            path = path.children[c]

    def search(self, word: str) -> bool:
        path = self.root
        for i, c in enumerate(word):
            if c in path.children:
                if i == len(word) - 1 and not path.children[c].eow:
                   return False
                path = path.children[c]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        path = self.root
        for i, c in enumerate(prefix):
            print(path.children, len(path.children))
            if c in path.children:
                path = path.children[c]
            else:
                return False
        return True

class TrieNode:

     def __init__(self, children=None, eow=False):
        self.children = {} if children is None else children
        self.eow = eow

    # def __init__(self, children={}, eow=False):
    #     self.children = children
    #     self.eow = eow