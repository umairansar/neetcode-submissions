class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {str(i+1) : chr(65 + i) for i in range(0, 26)}
        n = len(s)
        if n == 1:
            return 1 if mapping.get(s) else 0

        memo = {}
        def countDecodes(i, j):

            if (i, j) in memo:        # use `in`, not .get()
                return memo[(i, j)] 

            if i == j:
                return 1 if mapping.get(s[i]) else 0
            
            if i == j - 1:
                return (1 if mapping.get(s[i:i+2]) else 0) + countDecodes(i+1, j) if mapping.get(s[i]) else 0 

            ways = 0
            if i <= j:
                #one
                print("1|", i, j, s[i], mapping.get(s[i]))
                if mapping.get(s[i]):
                    print(i+1, j, ways)
                    cached = memo.get((i+1, j))
                    if cached:
                        ways += cached
                    else:
                        memo[(i+1, j)] = countDecodes(i+1, j)
                        ways += memo[(i+1, j)]
                    print(i+1, j, ways)

                #two
                print("2|", i, j, s[i:i+2], mapping.get(s[i:i+2]))
                if mapping.get(s[i:i+2]):
                    print(i+2, j, ways)
                    cached = memo.get((i+2, j))
                    if cached:
                        ways += cached
                    else:
                        memo[(i+2, j)] = countDecodes(i+2, j)
                        ways += memo[(i+2, j)]
                    print(i+2, j, ways)
                
                return ways
            
            return 1
            
        if n == 2:
            return (1 if mapping.get(s) else 0) + countDecodes(1, 1) if mapping.get(s[0]) else 0
        
        return countDecodes(0, n-1)