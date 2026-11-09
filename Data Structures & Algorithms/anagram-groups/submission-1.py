class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        # i need a dict with key counter of letters in a word and value words

        
        ana = {}
        for s in strs:
            rep = ''.join(sorted(s))
            if rep not in ana:
                ana[rep] = []
            ana[rep].append(s)


        ans = []

        for k in ana.values():
            ans.append(k)

        return ans



















        
        
        # mappings = {}
        # for s in strs:
        #     if "".join(sorted(s)) in mappings.keys():
        #         mappings["".join(sorted(s)) ].append(s)
        #     else:
        #         mappings["".join(sorted(s)) ] = [s]

        # # print(list(mappings.values()))

        # return list(mappings.values())