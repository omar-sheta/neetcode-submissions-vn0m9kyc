class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        # [-4, -1, -1, 0, 1, 2]

        # -4 target +4
        ans = set()
        for i in range(len(nums)-1):
            l = i+1
            target = -nums[i]
            r = len(nums) - 1
            while l<r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    ans.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1

        ans_list = [list(t) for t in ans]
        return ans_list

            


