class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, remain):
            if remain == 0:
                return 1

            if i == len(coins) or remain < 0:
                return 0

            if (i, remain) in memo:
                return memo[(i, remain)]

            memo[(i, remain)] = (
                dp(i + 1, remain) +
                dp(i, remain - coins[i])
            )

            return memo[(i, remain)]

        return dp(0, amount)