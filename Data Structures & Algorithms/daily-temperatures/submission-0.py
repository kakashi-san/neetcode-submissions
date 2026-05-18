class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        stk = []

        res = [0] * len(temperatures)

        for idx1, temp in enumerate(temperatures):
            while stk and temp > stk[-1][1]:
                    idx2, temperature = stk.pop()
                    res[idx2] = idx1 - idx2
            
            stk.append((idx1, temp))

        return res