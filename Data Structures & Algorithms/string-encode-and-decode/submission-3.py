class Solution:




    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return ""

        ans = ""
        for s in strs:
            ans += f'{len(s)}#{s}'

        return ans

    def decode(self, s: str) -> List[str]:
        # case it is empty
        if len(s) == 0:
            return []

        # Otherwise I need to decode by doing two things 
        # add digits to a num string until # then slice from # position to  position + the num then add it to res. 
        # repeat till end of s.
        ans = []
        i = 0

        print(s)
        while i<len(s):
            n = ""
            while s[i].isnumeric():
                n+=s[i]
                i+=1
            # print('done')
            # print(s[i])
            # print(n)
            n = int(n)
            if s[i] == '#':
                i+=1
                # print(s[i:i+num])
                ans.append(s[i:i+n])
                i = i+n
            
        return ans





        




