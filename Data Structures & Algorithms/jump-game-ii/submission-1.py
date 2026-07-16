class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(j):
            if j >= len(nums) - 1:
                return 1

            if j in memo:
                return memo[j]

            if nums[j] == 0:
                memo[j] = float('inf')
                return float('inf')

            min_count = float('inf')
            for i in range(1, nums[j] + 1):
                min_count = min(dp(i + j), min_count)

            memo[j] = 1 + min_count
            return memo[j]

        return dp(0) - 1