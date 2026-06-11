class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._min_stack or (self._min_stack and self._min_stack[-1][1] >= val):
            idx = len(self._stack)
            self._min_stack.append((idx, val))


    def pop(self) -> None:
        if self._stack:
            popped = self._stack.pop()
        
        if self._min_stack  and self._min_stack[-1][1] == popped:
            self._min_stack.pop()
        
        return popped

    def top(self) -> int:
        
        if self._stack:
            return self._stack[-1]
        
        return -1

    def getMin(self) -> int:
        if self._min_stack:
            return self._min_stack[-1][1]
        
        return -1
