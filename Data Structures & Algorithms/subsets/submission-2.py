class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(nums):
            if not nums: return [[]]

            first = nums[0]
            subsets_wo_first = rec(nums[1:])
            res = []
            for combo in subsets_wo_first:
                res.append([first, *combo])
            
            return res + subsets_wo_first
        
        return rec(nums)