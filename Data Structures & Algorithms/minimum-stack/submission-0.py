class MinStack:

    def __init__(self):
        self._list = []
        self._min_stk = []

    def push(self, val: int) -> None:
        self._list.append(val)
        if not self._min_stk:
            self._min_stk.append(val)
        elif self._min_stk[-1] < val:
            self._min_stk.append(self._min_stk[-1])
        
        else:
            self._min_stk.append(val)

    def pop(self) -> None:
        self._list.pop()
        self._min_stk.pop()        

    def top(self) -> int:
        return self._list[-1] if self._list else -1
        

    def getMin(self) -> int:
        return self._min_stk[-1]
        
