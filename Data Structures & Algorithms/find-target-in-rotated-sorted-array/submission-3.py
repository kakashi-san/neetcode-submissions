class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1

            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid
            return r
        
        inflex_pt = findMin(nums)
        l, r = 0, inflex_pt - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1

        l, r = inflex_pt, len(nums) - 1 

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1