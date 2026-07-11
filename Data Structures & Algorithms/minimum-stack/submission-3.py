class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min_stack and self._min_stack[-1] >= val:
            self._min_stack.append(val)

        elif not self._min_stack:
            self._min_stack.append(val)

    def pop(self) -> None:
        if self._stack:
            popped = self._stack.pop()
            if self._min_stack and self._min_stack[-1] == popped:
                self._min_stack.pop()
            return popped
        return -1

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]
        return -1

    def getMin(self) -> int:
        if self._min_stack:
            return self._min_stack[-1]
        
        return -1
