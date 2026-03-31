class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 100000
        for n in nums:
            smallest = min(smallest,n)
        
        return smallest