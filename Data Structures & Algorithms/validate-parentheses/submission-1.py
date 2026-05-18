class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }
        stk = []

        for char in s:
            if char in brace_map.keys():
                stk.append(char)
            else:
                if stk:
                    popped = stk.pop()
                else: return False
                if brace_map[popped] != char:
                    return False
        if stk:
            return False
        
        return True
                