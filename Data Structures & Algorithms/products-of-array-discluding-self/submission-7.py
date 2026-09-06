class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # nums = [1,2,4,6]

        ans = [0]*n

        # we need the product of everything before and after i (non-inclusive)
        pre = 1

        # this loops over nums and ans
        # get the prefix multiplication
        # at i = 0 mul = 1
        # update pre
        # put it in ans
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]



        # loop over ans from the other way around
        # every number in ans is missing the postfix multiplication
        # meaning that n-1 is missing nothing so put it in ans
        # n-2 is missing n-1
        # n-3 is missing n-2 and n-1.
        # the way postfix works is by storing the accumulated multiplication from n-1, 1 in order
        pos = 1
        for i in range(n-1,-1,-1):
            ans[i] *= pos
            pos *= nums[i] # get the postfix mul. starting n-1

        return ans
        

        
