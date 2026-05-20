class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for str_ in strs:
            normed_str = "".join(sorted(str_))

            if normed_str not in hash_map:
                hash_map[normed_str] = []

            hash_map[normed_str].append(
                str_
            )
        
        return list(hash_map.values())