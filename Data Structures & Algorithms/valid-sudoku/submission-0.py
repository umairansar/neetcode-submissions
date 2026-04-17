class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {i: set() for i in range(9)}
        colHash = {i: set() for i in range(9)}
        blockHash = {i: set() for i in range(9)}

        def getBlock(x, y):
            r = x // 3
            c = y // 3
            return r + 3 * c

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col in rowHash[i]:
                    return False
                if col in colHash[j]:
                    return False
                if col in blockHash[getBlock(i, j)]:
                    return False

                if col != ".":
                    rowHash[i].add(col)
                    colHash[j].add(col)
                    blockHash[getBlock(i, j)].add(col)

        return True