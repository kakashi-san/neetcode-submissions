class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i, curr_sum):
            if i >= len(coins) or curr_sum > amount:
                return float('inf')

            if curr_sum == amount:
                return 0
            
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            way1 = dp(i + 1, curr_sum)
            
            way2 = 1 + dp(0, curr_sum + coins[i])

            total = min(way1, way2)

            memo[(i, curr_sum)] = total

            return total

        res = dp(0, 0)

        return -1 if res == float('inf') else res