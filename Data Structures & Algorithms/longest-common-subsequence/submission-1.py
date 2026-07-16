class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}                                    # <-- was missing entirely

        def dp(t1, t2):
            if (t1, t2) in memo:
                return memo[(t1, t2)]

            if len(t1) == 0 or len(t2) == 0:
                memo[(t1, t2)] = 0                    # <-- base case wasn't cached either
                return 0

            if t1.startswith(t2[0]):
                result = 1 + dp(t1[1:], t2[1:])
            else:
                result = max(dp(t1[1:], t2), dp(t1, t2[1:]))

            memo[(t1, t2)] = result                   # <-- write to cache before returning
            return result

        return dp(text1, text2)