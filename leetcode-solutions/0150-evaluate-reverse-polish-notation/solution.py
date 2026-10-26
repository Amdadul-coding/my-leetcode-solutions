class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b-a)
            elif c == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == "/":
                c, d = int(stack.pop()), int(stack.pop())
                stack.append(int(d/c))
            else:
                stack.append(c)
        return int(stack.pop())


