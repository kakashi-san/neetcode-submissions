class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            
            seen[s[j]] = seen.get(s[j], 0) + 1

            while seen[s[j]] >= 2:
                seen[s[i]] -= 1
                if seen[s[i]] == 0:
                    del seen[s[i]]
                i += 1
            max_len = max(j - i + 1, max_len)
        
        return max_len
