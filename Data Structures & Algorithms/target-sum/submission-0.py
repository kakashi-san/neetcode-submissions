class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dp(i, curr_sum):
            if i == len(nums) and curr_sum == target:
                return 1

            if i >= len(nums):
                return 0

            way1 = dp(i + 1, curr_sum - nums[i])
            way2 = dp(i + 1, curr_sum + nums[i])

            return way1 + way2
        
        return dp(0, 0)