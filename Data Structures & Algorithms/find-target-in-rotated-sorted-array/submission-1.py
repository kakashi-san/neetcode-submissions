class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_inflexion(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return r

        def binary_search(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        inflexion_idx = search_inflexion(nums)

        if inflexion_idx == 0:
            return binary_search(nums, target)

        if target >= nums[0]:
            return binary_search(nums[:inflexion_idx], target)

        nxt = binary_search(nums[inflexion_idx:], target)
        return -1 if nxt == -1 else inflexion_idx + nxt