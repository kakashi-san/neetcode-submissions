class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        memo = {}

        def dp(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if curr_sum == target:
                return [[]]
            
            if curr_sum > target or i >= len(nums):
                return []

            combos_without_current = dp(i + 1, curr_sum)

            combos_with_current = dp(i, curr_sum + nums[i])
            ret = []

            for combo in combos_with_current:
                ret.append([nums[i], *combo])

            memo[(i, curr_sum)] = [*ret, *combos_without_current]

            return  memo[(i, curr_sum)]

        
        return dp(0, 0)






            