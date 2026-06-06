class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1: return True

        counter1 = {}
        counter2 = {}
        i = 0
        max_len = 0

        for j in range(len(s1)):
            counter1[s1[j]] = counter1.get(s1[j], 0) + 1

        for j in range(len(s2)):
            counter2[s2[j]] = counter2.get(s2[j], 0) + 1

            while j - i + 1 > len(s1):
                counter2[s2[i]] -= 1
                if counter2[s2[i]] == 0:
                    del counter2[s2[i]]
                i += 1

            if counter2 == counter1:
                return True

        return False                