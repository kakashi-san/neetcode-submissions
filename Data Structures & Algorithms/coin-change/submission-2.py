class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if curr_sum == amount:
                return 0
            if curr_sum > amount or i >= len(coins):
                return float('inf')

            take = 1 + dp(0, curr_sum + coins[i])
            skip = dp(i + 1, curr_sum)

            n = min(take, skip)
            memo[(i, curr_sum)] = n
            return n

        ans = dp(0, 0)

        return ans if ans != float('inf') else -1