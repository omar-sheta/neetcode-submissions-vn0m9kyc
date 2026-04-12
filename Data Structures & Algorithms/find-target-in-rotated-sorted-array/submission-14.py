class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = (l + r)//2

            if nums[mid]>nums[r]:
                l = mid + 1
            else:
                r = mid
        
        start = l

        l, r = 0, len(nums) - 1

        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r  = start

        if nums[start] == target:
            return start
        print(start)
        
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
                
        


