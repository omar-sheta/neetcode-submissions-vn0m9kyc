class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        largest = 0

        l = 0
        r = 0
        letters = {}

        for r in range(len(s)):
            letters[s[r]] = 1 + letters.get(s[r], 0)
            
            # now check if the window if valid
            # check if window size - max occurence of a letter is less than k meaning that if less, we can replace these letters to match the letter with maximum occ.
            # we invalidate the window if more values needs to be replaced than k
            while (r - l + 1) - max(letters.values()) > k:
                letters[s[l]] -= 1
                l+=1
            largest = max(r-l+1, largest)
            



        return largest

        