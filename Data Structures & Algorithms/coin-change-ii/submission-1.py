from typing import List
from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dp(i, curr_sum):
            if curr_sum == amount:
                return 1

            if i >= len(coins) or curr_sum > amount:
                return 0

            skip = dp(i + 1, curr_sum)
            take = dp(i, curr_sum + coins[i])

            return skip + take

        result = dp(0, 0)
        dp.cache_clear()  # avoid stale cache across multiple calls with different coins/amount
        return result