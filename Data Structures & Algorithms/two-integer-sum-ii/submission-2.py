class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return -1
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[r] + numbers[l]
            if total == target:

                return [l + 1, r + 1]

            if  total > target:
                r -= 1
            
            else:
                l += 1

        return -1