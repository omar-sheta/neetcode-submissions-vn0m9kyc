class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = {} # contains comp : index

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complements.keys():
                return [complements[comp], i]
            complements[nums[i]] = i


