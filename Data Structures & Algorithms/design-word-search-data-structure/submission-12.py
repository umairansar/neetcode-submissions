class WordDictionary: # Very careful with 0 and 1 length check on string

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        path = self.root
        for i, c in enumerate(word):
            if c not in path.children:
                path.children[c] = TrieNode()
            if i == len(word) - 1:
                print("setting", c, " to true")
                path.children[c].eow = True
            path = path.children[c]
        
    def search(self, word: str) -> bool:

        def searchChar(w, path):
            if len(w) == 0: # Very Careful, path is set to end when string consumed
                return path.eow
            
            c = w[0]
            if c == ".":
                res = False 
                w = w[1:]
                for k in list(path.children.keys()):
                    p = path.children[k]
                    res |= searchChar(w, p)
                return res
            elif c in path.children:
                p = path.children[c]
                w = w[1:]
                return searchChar(w, p)
            else:
                return False

        return searchChar(word, self.root)

        # path = self.root
        # for i, c in enumerate(word):
        #     if c in path.children:
        #         if i == len(word) - 1 and not path.children[c].eow:
        #            return False
        #         path = path.children[c]
        #     elif c == "." and list(path.children.keys()):
        #         anyKey = list(path.children.keys())[0]
        #         path = path.children[anyKey]
        #     else:
        #         return False
        # return True
        
class TrieNode:

     def __init__(self, children=None, eow=False):
        self.children = {} if children is None else children
        self.eow = eow