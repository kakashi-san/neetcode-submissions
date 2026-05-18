class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return [[]]

        first = nums[0]

        subsets_wo_first = self.subsets(
            nums[1:]
        )
        result = []
        for sub in subsets_wo_first:
            result.append(
                [*sub, first]
            )
        return result + subsets_wo_first