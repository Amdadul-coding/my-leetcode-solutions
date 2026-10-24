class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        openBrackets = set(['{', '[', '('])
        for c in s:
            if c in openBrackets:
                stack.append(c)
            elif c not in openBrackets:
                if not stack:
                    return False
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return not stack
