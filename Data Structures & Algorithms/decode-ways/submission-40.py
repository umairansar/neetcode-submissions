class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {str(i+1) : chr(65 + i) for i in range(0, 26)}
        n = len(s)

        memo = {}
        def countDecodes(i, j):

            if (i, j) in memo:
                return memo[(i, j)] 
                
            if i == j:
                return 1 if mapping.get(s[i]) else 0
            
            if i == j - 1:
                return (1 if mapping.get(s[i:i+2]) else 0) + countDecodes(i+1, j) if mapping.get(s[i]) else 0 

            ways = 0
            if i < j:
                #one
                if mapping.get(s[i]):
                    cached = memo.get((i+1, j))
                    if cached:
                        ways += cached
                    else:
                        memo[(i+1, j)] = countDecodes(i+1, j)
                        ways += memo[(i+1, j)]

                #two
                if mapping.get(s[i:i+2]):
                    cached = memo.get((i+2, j))
                    if cached:
                        ways += cached
                    else:
                        memo[(i+2, j)] = countDecodes(i+2, j)
                        ways += memo[(i+2, j)]
                
                return ways
        
        return countDecodes(0, n-1)