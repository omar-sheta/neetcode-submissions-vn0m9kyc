class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l<r:
            mid = l + (r-l)//2
            
            # [3,4,5,6,1,2]
            # print(f"nums[mid]->{nums[mid]}")
            # print(f"nums[l]->{nums[l]}")
            # print(f"nums[r]->{nums[r]}")
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        return nums[l]





            