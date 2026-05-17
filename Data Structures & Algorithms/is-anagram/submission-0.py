class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}

        for char in s:
            s_set[char] = s_set.get(char, 0) + 1
        
        for char in t:
            if char not in s_set:
                return False
            s_set[char] -= 1
            if s_set[char] == 0:
                del s_set[char]
        
        if s_set:
            return False
        
        else:
            return True