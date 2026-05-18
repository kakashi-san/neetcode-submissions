class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        seen = set()

        for i in range(len(nums) - 1 ):

            l, r = i + 1, len(nums) - 1
            while l < r :
                if nums[l] + nums[r] + nums[i] == 0 and (
                    nums[l], nums[r], nums[i]
                    ) not in seen :
                    res.append(
                        [nums[i], nums[l], nums[r]]
                    )
                    seen.add(
                     (nums[l], nums[r], nums[i])   
                    )
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1

                else :
                    l += 1
        return res