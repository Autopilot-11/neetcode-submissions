from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[i] == ')' and not top == '(':
                    return False
                if s[i] == '}' and not top == '{':
                    return False
                if s[i] == ']' and not top == '[':
                    return False
        return len(stack) == 0