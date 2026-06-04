class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def satisfies_k_replacement(counter, window_size):
            max_len = 0
            for char in counter:
                max_len = max(counter[char], max_len)
            
            flag = window_size - max_len <= k
            return flag

        counter = {}
        i = 0
        longest = 1
        for j in range(len(s)):
            counter[s[j]] = counter.get(s[j], 0 ) + 1

            while not satisfies_k_replacement(counter, j - i + 1):
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            longest = max(longest, j - i + 1)

        return longest