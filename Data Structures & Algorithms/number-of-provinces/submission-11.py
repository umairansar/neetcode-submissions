class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(n):
            if n != parents[n]:
                parents[n] = parents[parents[n]]
                return find(parents[n])
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            else:
                if ranks[p1] > ranks[p2]:
                    parents[p2] = p1
                    ranks[p1] += ranks[p2]
                else:
                    parents[p1] = p2
                    ranks[p2] += ranks[p1]
                return True


        row = len(isConnected)
        col = len(isConnected[0])
        result = row
        parents = [i for i in range(row)]
        ranks = [1] * row
        for i in range(row):
            for j in range(i+1, col):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        result -= 1

        return result                      
                    

