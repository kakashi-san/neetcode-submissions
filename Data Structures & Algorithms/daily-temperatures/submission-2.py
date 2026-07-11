class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop_idx, pop_val = stack.pop()
                res[pop_idx] = idx - pop_idx

            stack.append((idx, temp))

        return res