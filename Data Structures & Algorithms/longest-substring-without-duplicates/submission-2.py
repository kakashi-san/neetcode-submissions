class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        def is_univ_valued(counter):

            for i in counter:
                if counter[i] > 1:
                    return False

            return True

        counter = {}
        longest = 1

        i = 0
        for j in range(len(s)):
            counter[s[j]] = counter.get(s[j], 0) + 1

            while not is_univ_valued(counter):
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            longest = max(longest, j - i + 1)
        
        return longest