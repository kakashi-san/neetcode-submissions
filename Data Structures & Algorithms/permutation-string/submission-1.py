class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if len(s1) == len(s2): return sorted(s1) == sorted(s2)

        s1_counter = {}
        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) + 1

        s2_counter = {}
        for char in s2[:len(s1)]:
            s2_counter[char] = s2_counter.get(char, 0) + 1
        
        if s1_counter == s2_counter:
            return True


        for j in range(1, len(s2) - len(s1) + 1):
            out = s2[j - 1]
            in_ = s2[j + len(s1) - 1]

            s2_counter[in_] = s2_counter.get(in_, 0) + 1
            s2_counter[out] -= 1
            if s2_counter[out] == 0:
                del s2_counter[out]

            if s1_counter == s2_counter:
                return True
        
        return False
        

