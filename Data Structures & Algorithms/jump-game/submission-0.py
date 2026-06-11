class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if nums[i] + i >= len(nums) - 1:
                return True

            for j in range(1, nums[i] + 1):
                if dp(i + j):
                    memo[i + j] = True
                    return True

            memo[i] = False

            return False

        return dp(0)