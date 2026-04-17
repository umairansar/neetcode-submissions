class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def factorial(n):
            if n == 0:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = n * factorial(n-1)
            return memo[n]

        Rs = n - 1
        Ds = m - 1
        total = Rs + Ds
        return factorial(total) // (factorial(Rs) * factorial(Ds))