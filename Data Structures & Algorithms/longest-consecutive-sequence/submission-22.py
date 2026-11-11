class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0
        count = 0

        # look for the start of the seq
        # then start counting
        for n in s:
            if n - 1 not in s: # this loop happens when there is a start of a seq.       
                # this is a start of the seq
                count += 1 # start counting
                # n now is the start of the seq.
                # check n + 1
                while n + 1 in s:
                    count += 1
                    n += 1
                longest = max(longest, count)
                count = 0
        
        return longest

