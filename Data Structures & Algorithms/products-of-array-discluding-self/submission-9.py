class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = []
        forward.append(1)
        prefix = nums[0]
        for i in range(1,len(nums)):
            # print(prefix, nums[i])
            forward.append(prefix)
            prefix *= nums[i]
        
        # I can either create a new array to store the backward or do it on the forward so I can save space

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # print(postfix, forward[i])
            forward[i]*=postfix
            postfix*=nums[i]

        return forward

