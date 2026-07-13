class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def rec(i, curr_sum):
            if i >= len(nums) or curr_sum > target:
                return []
            
            if curr_sum == target:
                return [[]]

            take = rec(i, curr_sum + nums[i])
            skip = rec(i + 1, curr_sum)

            ret = []

            for combo in take:
                ret.append(
                    [nums[i], *combo]
                )
            
            return [*ret, *skip] 
        
        return rec(0, 0)