class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        max_len = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                i = 0
                while num + i in nums_set:
                    i += 1
                    max_len = max(max_len, i)

        return max_len