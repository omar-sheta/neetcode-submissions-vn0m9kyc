class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = {}
        for s in strs:
            if "".join(sorted(s)) in mappings.keys():
                mappings["".join(sorted(s)) ].append(s)
            else:
                mappings["".join(sorted(s)) ] = [s]

        # print(list(mappings.values()))

        return list(mappings.values())