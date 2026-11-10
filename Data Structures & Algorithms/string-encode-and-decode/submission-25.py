class Solution:
# my mistake was not knowing that the loop keeps a local counter that is not changing when it loops.
# Also, I did not consider numbers >9 as the size.
# I spent about 20 mins on this 
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            n = len(s)
            encoded_string+=f'{n}#{s}'
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        print(s)
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                n = ''
                while s[i]!='#':
                    n += s[i]
                    i+=1
                n = int(n)

                encoded = ""
                for k in range(n):
                    encoded += s[i+1]
                    i+=1
                strs.append(encoded)
            i+=1
        
        return strs

