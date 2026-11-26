class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # my initial thoughts here
        # slide a window of size s1 over s2
        # collect this window from s2 as a set, check if this set is equal to the
        # set of s1
        # if yes return true

        s1_count = Counter(s1)
        # set does not work in the sense of words with duplicate letters
        # a counter would work better
        for i in range(len(s2)):
            s2_counter = Counter(s2[i:i+len(s1)])
            if s1_count == s2_counter:
                return True

        return False
