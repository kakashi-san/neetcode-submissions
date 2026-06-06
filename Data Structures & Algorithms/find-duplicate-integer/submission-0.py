class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            lookup_idx = abs(num) - 1

            if nums[lookup_idx] < 0:
                return abs(num)

            nums[lookup_idx] *= -1