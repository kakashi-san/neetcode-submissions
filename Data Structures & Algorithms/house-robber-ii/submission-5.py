class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def rob_helper(nums: List[int]) -> int:
            memo = {}
            def dp(i):
                if i >= len(nums):
                    return 0

                if i in memo:
                    return memo[i]
                
                rob1 = nums[i] + dp(i + 2)
                rob2 = dp(i + 1)

                memo[i] = max(rob1, rob2)

                return max(rob1, rob2)

            return dp(0)

        return max(
            rob_helper(nums[1:]),
            rob_helper(nums[:-1])
        )