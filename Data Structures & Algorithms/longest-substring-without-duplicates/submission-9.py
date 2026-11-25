class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a seen set to check if no dup?
        # will try this approach
        # slide the window to include more chars
        # if a duplicate is found
        # move the window to that place

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        longest = 1
        l = 0
        r = l+1

        seen = set(s[l])
        while r<len(s):
            while r<len(s) and s[r] not in seen:
                seen.add(s[r])
                r+=1

            count = r-l
            longest = max(count, longest)
            while r<len(s) and s[r] in seen:
                seen.remove(s[l])
                l+=1

        return  longest
            


