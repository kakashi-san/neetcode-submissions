class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_count = 0
        i = 0
        max_len = 0

        for j in range(len(s)):
            counter[s[j]] = counter.get(s[j], 0) + 1
            max_count = max(max_count, counter[s[j]])

            while j - i + 1 - max_count > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]] 
                i += 1
            max_len = max(max_len, j - i + 1)
        
        return max_len
            