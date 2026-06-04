class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}

        for string in strs:
            x_formed = "".join(sorted(string))
            if x_formed not in string_map:
                string_map[x_formed] = []

            string_map[x_formed].append(string)
        
        return list(string_map.values())