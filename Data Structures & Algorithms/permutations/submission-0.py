class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(nums):
            if not nums:
                return [[]]

            first = nums[0]
            permutations_without_first = rec(nums[1:])

            res = []
            for perm in permutations_without_first:
                for i in range(len(perm) + 1):
                    res.append(
                        [*perm[i:], first, *perm[:i]]
                    )
            return res

        return rec(nums)