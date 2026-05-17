class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            if "".join(sorted(string)) not in group:
                group["".join(sorted(string))] = []

            group["".join(sorted(string))].append(string)
        
        return list(group.values())