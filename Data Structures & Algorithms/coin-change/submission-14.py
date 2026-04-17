class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def consume(target):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            ways = []
            for coin in coins:
                if target - coin >= 0:
                    way = consume(target - coin)
                    if way >= 0:
                        ways.append(1 + way)
           
            memo[target] = min(ways) if len(ways) > 0 else -1
            return memo[target]

        return consume(amount)
        
