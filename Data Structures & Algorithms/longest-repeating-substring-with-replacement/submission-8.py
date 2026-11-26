class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        largest = 0

        l = 0
        r = 0
        letters = {}
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r],0) + 1
            while (r - l + 1) - max(letters.values())>k:
                letters[s[l]] -= 1
                l+=1
            largest = max(r - l + 1, largest)



        return largest

        