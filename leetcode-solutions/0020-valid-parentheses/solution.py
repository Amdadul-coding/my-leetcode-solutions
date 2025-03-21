class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and '(' in stack and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and '[' in stack and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and '{' in stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True
