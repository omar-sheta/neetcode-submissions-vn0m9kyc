class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        ans = ""
        for s in strs:
            ans += f'{len(s)}#{s}'
        return ans

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ans, i = [], 0

        while i<len(s):
            l = ""
            while s[i].isnumeric():
                l+=s[i]
                i+=1
            if s[i] == "#":
                i+=1
                st = s[i:i+int(l)]
                i += int(l) - 1
                ans.append(st)
            i += 1
            
        return ans
                


        




