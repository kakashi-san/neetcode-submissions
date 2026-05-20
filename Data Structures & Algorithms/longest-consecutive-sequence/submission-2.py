class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 0
                i = 0
                while num + i in nums_set:
                    count += 1
                    i += 1
                
                max_len = max(max_len, count)
        
        return max_len