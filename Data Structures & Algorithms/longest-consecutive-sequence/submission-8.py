class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        count = 0
        s = set(nums)

        for i in s:
            if i - 1 in s:
                continue
            else:
                # this is a start of a sequence
                # check if i + 1 exist
                # print('start')
                while i in s:
                    print(i)
                    count +=1
                    # print('count ',count)
                    i = i+1
                longest = max(longest, count)
                count = 0
        

        return longest
