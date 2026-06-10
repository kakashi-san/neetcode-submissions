class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        memo = {}

        def dp(i):
            if i >= len(nums):
                return [[]]

            if i in memo:
                return memo[i]

            combos_without_first = dp(i + 1)

            res = []
            for combo in combos_without_first:
                add = tuple(sorted([nums[i], *combo]))
                if add not in seen:
                    res.append(list(add))
                seen.add(add)

            memo[i] = combos_without_first + res

            return memo[i]
        
        return dp(0)