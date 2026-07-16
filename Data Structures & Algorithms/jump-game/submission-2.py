import sys
sys.setrecursionlimit(10000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dp(j):
            if j >= len(nums) - 1:
                return True

            if j in memo:
                return memo[j]

            if nums[j] == 0:
                memo[j] = False
                return False

            for i in range(1, nums[j] + 1):
                if dp(j + i):
                    memo[j] = True
                    return True

            memo[j] = False
            return False

        return dp(0)