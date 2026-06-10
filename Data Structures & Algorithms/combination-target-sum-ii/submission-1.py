class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        memo = {}


        def dp(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
                
            if curr_sum == target:
                return [[]]

            if i >= len(candidates) or curr_sum > target:
                return []


            combo_with_first = dp(i + 1, curr_sum + candidates[i])

            j = i + 1

            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            combo_without_first = dp(j , curr_sum)

            res = []

            for combo in combo_with_first:
                res.append([candidates[i], *combo])

            memo[(i, curr_sum)] = [*res, *combo_without_first]
 
            return memo[(i, curr_sum)]

        return dp(0, 0)