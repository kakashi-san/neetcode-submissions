class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(rem_str):
            if rem_str in memo:
                return memo[rem_str]

            if len(rem_str) == 0:
                return True

            for word in wordDict:
                if rem_str.startswith(word):
                    if dp(rem_str[len(word):]):
                        memo[rem_str] = True
                        return True

            memo[rem_str] = False
            return False

        return dp(s)