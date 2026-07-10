class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen =  set()
        j = 0
        max_len = 1

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1

            seen.add(s[i])
            max_len = max(i - j + 1, max_len)
        
        return max_len
