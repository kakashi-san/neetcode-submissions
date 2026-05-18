class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def analyse_dict(counter):
            total_len = 0
            max_count = 0
            for char in counter:
                total_len += counter[char]
                max_count = max(max_count, counter[char])
            
            return total_len - max_count

        
        max_len = 0
        i = 0
        counter = {}

        for j in range(len(s)):
            counter[s[j]] = counter.get(s[j], 0) + 1
            while analyse_dict(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            max_len = max(max_len, j - i + 1)

        return max_len
