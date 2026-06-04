class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = 1
        forward_prop = []
        for num in nums:
            forward_prop.append(forward)
            forward = forward * num

        backward = 1
        backward_prop = []
        for num in nums[::-1]:
            backward_prop.append(backward)
            backward = backward * num

        backward_prop.reverse()

        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(backward_prop[i])
            elif i == len(nums) - 1:
                res.append(forward_prop[i])
            else:
                res.append(forward_prop[i] * backward_prop[i])
        
        return res