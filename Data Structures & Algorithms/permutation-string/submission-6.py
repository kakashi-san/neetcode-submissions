class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = {}
        ref_counter = {}

        for ch in s1:
            ref_counter[ch] = ref_counter.get(ch, 0) + 1

        i = 0
        for j in range(len(s2)):
            counter[s2[j]] = counter.get(s2[j], 0) + 1

            while j - i + 1 > len(s1):
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    del counter[s2[i]]
                i += 1

            if counter == ref_counter:
                return True

        return False