class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = self.solveNQueensAgain(n, n, [])
        return self.solutionsMapped(n, solutions)

    def solutionsMapped(self, n:int, solutions: List[Tuple[int, int]]) -> List[List[str]]:
        solutions_mapped = []
        for solution in solutions:
            solution_mapped = []
            for x, y in solution:
                temp = ""
                for k in range(n):
                    if k == y:
                        temp = temp+"Q"
                    else:
                        temp = temp+"."
                solution_mapped.append(temp)
            solutions_mapped.append(solution_mapped)
        return solutions_mapped

    def solveNQueensAgain(self, queen_count: int, n: int, occupied_blocks : List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if queen_count == 0:
            return []

        output = []
        # for i in range(n):
        i = queen_count - 1 # place 1st queen in 1st row, 2nd in 2nd and so on
        for j in range(n):
            print(i, j, occupied_blocks)
            if self.noCollision(i, j, occupied_blocks):
                queen_placed_at = (i, j)
                res = self.solveNQueensAgain(queen_count - 1, n, occupied_blocks + [(i, j)])
        
                if len(res) == 0 and queen_count == 1:
                    output.append([queen_placed_at])
                else:
                    for r in res:
                        if len(r) == (queen_count - 1):
                            out = [queen_placed_at] + r
                            output.append(out)
        
        return output        

    def noCollision(self, i:int, j:int, occupied_blocks : List[Tuple[int, int]]) -> bool:
        if (i, j) in occupied_blocks:
            return False
        
        for (x, y) in occupied_blocks:
            k1 = abs(i - x)
            k2 = abs(j - y)

            #up down case
            if (k1 > 0 and k2 == 0) or (k1 ==  0 and k2 > 0):
                return False
            
            #diagonal case
            if (k1 == k2):
                return False
        
        return True
        