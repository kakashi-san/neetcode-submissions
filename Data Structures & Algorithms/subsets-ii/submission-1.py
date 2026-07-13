class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def rec(i):
            if i == len(nums) - 1:
                return [[]]
            

            first =  nums[i]
            subsets_wo_first = rec(i + 1)

            res = []

            for combo in subsets_wo_first:
                res.append(
                    [*combo, first]
                )
            
            return res + subsets_wo_first

        subs = rec(-1)
        seen = set()
        res = []
        for sub in subs:
            sub.sort()                 # sort in place
            key = tuple(sub)           # now safe to use as a dict/set key
            if key in seen:
                continue
            seen.add(key)
            res.append(sub)            # append the actual sorted list, not sub.sort()

        return res