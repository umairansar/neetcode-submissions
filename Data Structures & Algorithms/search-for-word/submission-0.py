class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def isAdjacent(box, i, j):
            if i == box[0] and ((j + 1) == box[1] or (j - 1) == box[1]):
                return True
            if j == box[1] and ((i + 1) == box[0] or (i - 1) == box[0]):
                return True
            return False

        def dfs(path, res, index):
            match = map(lambda x: board[x[0]][x[1]], path)
            match = "".join(match)
            print(match, path)
            if match == word:
                res.append(path.copy())
                return 

            for i in range(rows):
                for j in range(cols):
                    if (i, j) in path:
                        continue
                    if board[i][j] != word[index]:
                        continue
                    # matches but adjescent
                    if len(path) == 0 or (len(path) > 0 and isAdjacent(path[-1], i, j)):
                        print("board[i][j]", board[i][j], "word[]", word[index])
                        path.append((i, j))
                        dfs(path, res, index+1)
                        #backtrack
                        path.remove((i, j))


        res = []
        dfs([], res, 0)
        return len(res) > 0