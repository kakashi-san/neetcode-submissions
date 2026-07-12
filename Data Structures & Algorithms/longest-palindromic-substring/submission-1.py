class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        if len(s) == 1: return s

        max_len = 1
        res = s[0]
        for i in range(len(s)):
            j = 0
            while i + j < len(s) and i - j >= 0 and s[i + j] == s[i - j]:
                curr_len = 2 * j + 1
                if max_len < curr_len:
                    res = s[i - j: i + j + 1]
                    max_len = curr_len
                j += 1

        for i in range(len(s)):
            j = 0
            while i + j + 1 < len(s) and i - j >= 0 and s[i + j + 1] == s[i - j]:
                curr_len = 2 * j + 2
                if max_len < curr_len:
                    res = s[i - j: i + j + 2]
                    max_len = curr_len
                j += 1

        return res