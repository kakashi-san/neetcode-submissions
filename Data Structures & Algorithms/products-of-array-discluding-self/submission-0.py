class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        curr = 1

        forward_prod = []

        for num in nums:
            forward_prod.append(curr)
            curr = curr * num

        curr = 1
        backward_prod = []

        for i in range(len(nums)):
            backward_prod.append(curr)
            curr = curr * nums[len(nums) - i - 1]

        backward_prod.reverse()

        result = []
        for i in range(len(nums)):
            result.append(forward_prod[i] * backward_prod[i])
        
        return result
 

