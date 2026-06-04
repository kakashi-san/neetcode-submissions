class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def rec(nums):
            
            if not nums:
                return [[]]
            
            first = nums[0]
            subsets_without_first = rec(nums[1:])
            res = []

            for combo in subsets_without_first:
                res.append(
                    [first, *combo]
                )
            return res + subsets_without_first
        
        return rec(nums)