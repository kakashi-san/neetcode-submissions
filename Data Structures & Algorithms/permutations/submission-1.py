class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(i):            
            if i == len(nums) - 1:
                return [[]]

            first = nums[i]
            perms_wo_first = rec(i + 1)
            res = []

            for perm in perms_wo_first:
                for j in range(len(perm) + 1):
                    res.append(
                        [*perm[:j], first, *perm[j:]]
                    )
            return res

        return rec(-1)
