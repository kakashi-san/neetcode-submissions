class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}

        for s in strs:
            norm = "".join(sorted(s))
            if norm not in map_dict:
                map_dict[norm] = []
            
            map_dict[norm].append(s)

        return list(map_dict.values())