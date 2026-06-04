class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        seen = set(nums)

        longest = 1

        for num in seen:
            if num - 1 not in seen:
                i = 1
                while num + i in seen:
                    i += 1
                    longest = max(longest, i)
        
        return longest