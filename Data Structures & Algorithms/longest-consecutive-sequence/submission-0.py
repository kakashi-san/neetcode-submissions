class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                i = 0
                while num + i in nums:
                    i += 1
                max_len = max(max_len, i)
        return max_len
