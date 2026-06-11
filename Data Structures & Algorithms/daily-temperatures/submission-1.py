class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                curr_idx, curr_temp = stack.pop()
                res[curr_idx] = idx - curr_idx
            
            stack.append((idx, temp))

        return res
