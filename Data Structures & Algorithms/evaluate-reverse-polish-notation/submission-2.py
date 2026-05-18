class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        def check_int(i):
            try:
                int(i)
                return True
            except:
                return False
        for token in tokens:
            if check_int(token):
                op_stack.append(int(token))

            elif token == "+":
                pop1 = op_stack.pop()
                pop2 = op_stack.pop()
                op_stack.append(
                    pop1 + pop2
                )
            elif token == "-":
                pop1 = op_stack.pop()
                pop2 = op_stack.pop()
                op_stack.append(
                    pop2 - pop1
                )
            elif token == "*":
                pop1 = op_stack.pop()
                pop2 = op_stack.pop()
                op_stack.append(
                    pop1 * pop2
                )
            elif token == "/":
                pop1 = op_stack.pop()
                pop2 = op_stack.pop()
                op_stack.append(
                    int(pop2 / pop1)
                )
        
        return op_stack[-1]

