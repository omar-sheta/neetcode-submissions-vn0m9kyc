class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The pattern [^a-zA-Z0-9] matches any character not in the set
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = 0
        r = len(s) - 1

        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True