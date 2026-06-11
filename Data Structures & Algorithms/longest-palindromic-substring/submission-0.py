class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        max_count = 1
        res = s[0]

        for i in range(len(s)):
            j, k = i, i
            count = -1  # because first expansion adds 2

            while j >= 0 and k < len(s) and s[j] == s[k]:
                count += 2

                if count > max_count:
                    res = s[j:k + 1]
                    max_count = count

                j -= 1
                k += 1

        for i in range(len(s)):
            j, k = i, i + 1
            count = 0

            while j >= 0 and k < len(s) and s[j] == s[k]:
                count += 2

                if count > max_count:
                    res = s[j:k + 1]
                    max_count = count

                j -= 1
                k += 1

        return res